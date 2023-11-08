from aiogram import types, Dispatcher
from create_bot import dp, bot

# Этот и последующие декораторы оставил для примера, т.к. использовал их в предыдущих версиях
#@dp.message_handler(commands=["start", "help"])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Приятного аппетита")
        await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему:\nhttps://t.me/pizza_bulka_bot")  # Если пользователь не авторизован в группе 

#@dp.message_handler(commands=["режим работы"])
async def pizza_open_command(message: types.Message):
        await bot.send_message(message.from_user.id, "ВС-Чт с 9:00 до 21:00б Пт-Сб с 10:00 до 22:00")

#@dp.message_handler(commands=["расположение"])
async def pizza_place_command(message: types.Message):
        await bot.send_message(message.from_user.id, "СПБ, ул. Любая 8")

#@dp.message_handler(commands=["Меню"])
#async def pizza_open_command(message: types.Message):
#      for ret in cur.execute('SELECT * FROM menu').fetchall():
#          await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\Цена" {ret[-1\]})

def register_handlers_client(dp : Dispatcher):
    # Функция для последующей регистраци клиентских хэндлеров в основном файле
    dp.register_message_handler(command_start, commands=['start', 'help'])    
    dp.register_message_handler(pizza_open_command, commands=['режим работы'])
    dp.register_message_handler(pizza_place_command, commands=['расположение'])
    

