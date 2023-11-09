from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

# Этот и последующие декораторы оставил для примера, т.к. использовал их в предыдущих версиях
#@dp.message_handler(commands=["start", "help"])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Приятного аппетита", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему:\nhttps://t.me/pizza_bulka_bot")  # Если пользователь не авторизован в группе 

#@dp.message_handler(commands=["режим работы"])
async def pizza_open_command(message: types.Message):
        await bot.send_message(message.from_user.id, "ВС-Чт с 9:00 до 21:00б Пт-Сб с 10:00 до 22:00")#, reply_markup=ReplyKeyboardRemove())

#@dp.message_handler(commands=["расположение"])
async def pizza_place_command(message: types.Message):
        await bot.send_message(message.from_user.id, "СПБ, ул. Любая 8")

#@dp.message_handler(commands=["Меню"])
async def pizza_menu_command(message: types.Message):
     await sqlite_db.sql_read(message)


# Функция для последующей регистраци клиентских хэндлеров в основном файле
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])    
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы', 'режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение', 'расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню', 'меню'])
   