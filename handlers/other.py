from aiogram import types, Dispatcher
import json, string
from create_bot import dp

#@dp.message_handler()
async def echo_send(message: types.Message):
    # Фильтр матов, хранящихся в файле cenz.json
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Маты в группе запрещены')
        await message.delete()

def register_handlers_other(dp : Dispatcher):
    # Функция для регистрации хэндлера матов в основном файле
    dp.register_message_handler(echo_send)   