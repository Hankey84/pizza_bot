from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle, ReplyKeyboardRemove
from data_base import sqlite_db
import hashlib

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

# Пример работы с лямбда функцией для парсинга текста на нужный топик, напримет "такси"
#@dp.message_handler(lambda message : message.text.startswith('такси'))
async def taxi_command(message: types.Message):
     await message.answer('Вам надо заказать такси?')

# Инлайн хендлер для поднятия из любой строки Телеграмма нашего бота и запрос в википедию по парсингу
#@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    text = query.query or "echo"
    link = 'https://ru.wikipedia.org/wiki/'+text
    result_id: str = hashlib.md5(text.encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(
         id = result_id,
         title='Статья Wikipedia:',
         url=link,
         input_message_content=types.InputTextMessageContent(
            message_text=link))]
    await query.answer(articles, cache_time=1, is_personal=True)


# Функция для последующей регистраци клиентских хэндлеров в основном файле
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])    
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы', 'режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение', 'расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню', 'меню'])
    dp.register_message_handler(taxi_command, lambda message : message.text.startswith('такси'))
    dp.register_inline_handler(inline_handler)
    