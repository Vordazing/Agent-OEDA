import routeros_api
from aiogram import types
from object.list import mikrotik_data
from aiogram.utils.keyboard import InlineKeyboardBuilder


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


async def work(callback: types.CallbackQuery):
    button_value = callback.data.replace('_', '')
    mikrotik_info = mikrotik_data.get(button_value)
    data_time = time_mikrotik(mikrotik_info['HOST'], mikrotik_info['USERNAME'], mikrotik_info['PASSWORD'])
    await callback.message.edit_text(text=f"Дата на микроте {button_value}: {data_time['date']}\n"
                                          f"Время на микроте {button_value}: {data_time['time']}")
    sent_address = None
    while True:
        data_list = fetch_address_lists(mikrotik_info['HOST'], mikrotik_info['USERNAME'], mikrotik_info['PASSWORD'])
        for entry in data_list:
            date_str, time_str = entry['creation-time'].split()
            if date_str == data_time['date'] and data_time['time'] <= time_str:
                if sent_address != entry['address']:
                    print(entry['address'], entry['creation-time'])
                    await callback.message.answer(text=f"{entry['address']}")
                    sent_address = entry['address']


