from aiogram import Bot, types
from aiogram.dispatcher import dispatcher
from aiogram.utils import executor

import os

bot = Bot(token=os.getenv('SECRET_TOKEN'))
dp = dispatcher(bot)

@dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == 'Привет':
        await message.answer('И тебе привет!') # simple reply
    #await message.reply(message.text)  # reply to smbdy
    #await bot.send_message(message.from_user.id, message.text)  #reply in own branch



executor.start_polling(dp, scip_updates=True)

