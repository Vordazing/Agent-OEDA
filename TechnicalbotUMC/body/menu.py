import routeros_api
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def choice_object(message: types.Message):
    builder = InlineKeyboardBuilder()
    button_list = ['ceh', 'ggp1', 'ggp2', 'ggp3', 'ggp4', 'ggp5',
                   'ggp6', 'kont1', 'kont2', 'kont3', 'kos1', 'kos2',
                   'kos3', 'kos4', 'kos5', 'kos6', 'kos7', 'kos8',
                   'kusa1', 'kusa2', 'rai0', 'rai1', 'rai2', 'rai3',
                   'rai6', 'rai7', 'rai8']

    for index in button_list:

        builder.button(text=f"{index}", callback_data=f"_{index}")

    await message.answer(text="👾Выберите микротик:", reply_markup=builder.as_markup())


async def on_start_command(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Начать прослушивание микротика на объекте🛂")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(text="👾Привет! Это технический бот, что хотите сделать ?", reply_markup=keyboard)
    await message.delete()