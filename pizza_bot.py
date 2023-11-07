from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor

import json, string
import os



bot = Bot(token=os.getenv('SECRET_TOKEN'))

dp = Dispatcher(bot)


async def on_startup(_):
    print("Бот вышел в онлайн")


"""*************** Clients part ***********************"""


@dp.message_handler(commands=["start", "help"])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Приятного аппетита")
        await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему:\nhttps://t.me/pizza_bulka_bot")


"""*************** Admin part *************************"""

"""**************** Common part ***********************"""


@dp.message_handler()
async def echo_send(message: types.Message):
    # Фильтр матов, хранящихся в файле cenz.json
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Маты в группе запрещены')
        await message.delete()
    
    #if message.text == "Привет":
    #    await message.answer("И тебе привет!")  # simple reply
    # await message.reply(message.text)  # reply to smbdy
    # await bot.send_message(message.from_user.id, message.text)  #reply in own branch


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
