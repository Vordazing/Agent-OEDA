import json
import os
import time

import routeros_api
from aiogram import types
from object.list import mikrotik_data
from aiogram.utils.keyboard import InlineKeyboardBuilder
from main import dp


def fetch_address_lists(host, username, password):
    api_pool = routeros_api.RouterOsApiPool(host=host, username=username, password=password, port=8728, plaintext_login=True)
    connection = api_pool.get_api()
    address_lists = connection.get_resource('/ip/firewall/address-list').get()
    return address_lists


def time_mikrotik(host, username, password):
    api_pool = routeros_api.RouterOsApiPool(host, username=username, password=password, port=8728, plaintext_login=True)
    connection = api_pool.get_api()
    response = connection.get_resource('/system/clock').get()
    mikrotik_time = response[0]
    return mikrotik_time


async def send_message(callback, mikrotik_info, data_time):
    sent_address = None
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Остановить",callback_data="stop"))
    user_file_path = 'body/user.json'
    start_time = time.time()
    message = await callback.message.answer(reply_markup=builder.as_markup(), text='👾Запускаю...')
    dots_count = 0

    while True:
        data_list = fetch_address_lists(mikrotik_info['HOST'], mikrotik_info['USERNAME'], mikrotik_info['PASSWORD'])
        if os.path.exists(user_file_path):
            with open(user_file_path, 'r') as json_file:
                user_data = json.load(json_file)
            if user_data.get("user_id") == callback.from_user.id and not user_data.get("flag", False):
                break

        for entry in data_list:
            date_str, time_str = entry['creation-time'].split()
            if date_str == data_time['date'] and data_time['time'] <= time_str:
                if sent_address != entry['address']:
                    print(entry['address'], entry['creation-time'])
                    await callback.message.answer(text=f"{entry['address']}")
                    sent_address = entry['address']
        elapsed_time = time.time() - start_time
        if elapsed_time > 60:
            break

        dots = "." * dots_count
        text_new = f'👾В работе {dots} 👾'
        await message.edit_text(text=text_new, reply_markup=builder.as_markup())
        dots_count = (dots_count + 1) % 4


async def work(callback: types.CallbackQuery):
    button_value = callback.data.replace('_', '')
    mikrotik_info = mikrotik_data.get(button_value)
    data_time = time_mikrotik(mikrotik_info['HOST'], mikrotik_info['USERNAME'], mikrotik_info['PASSWORD'])
    user_file_path = 'body/user.json'

    if os.path.exists(user_file_path):
        with open(user_file_path, 'r') as json_file:
            user_data = json.load(json_file)

        if user_data.get("user_id") == callback.from_user.id:
            user_data["flag"] = True
        else:
            user_data = {
                "user_id": callback.from_user.id,
                "flag": True
            }
    else:
        user_data = {
            "user_id": callback.from_user.id,
            "flag": True
        }
    with open(user_file_path, 'w') as json_file:
        json.dump(user_data, json_file)

    await callback.message.edit_text(text=f"Дата на микроте {button_value}: {data_time['date']}\n"
                                          f"Время на микроте {button_value}: {data_time['time']}")
    await send_message(mikrotik_info=mikrotik_info, data_time=data_time, callback=callback)


async def stop(callback: types.CallbackQuery):
    user_file_path = 'body/user.json'
    with open(user_file_path, 'r') as json_file:
        user_data = json.load(json_file)
        if user_data.get("user_id") == callback.from_user.id:
            user_data["flag"] = False
            with open(user_file_path, 'w') as json_file:
                json.dump(user_data, json_file)

    await callback.message.answer('Прослушивание остановлено 🔐')



