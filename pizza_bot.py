from aiogram.utils import executor
from create_bot import dp


async def on_startup(_):
    # Здесь будут выводиться данные при запуске бота в терминал
    print("Бот вышел в онлайн")

from handlers import client, admin, other

# Регистрируем наши хэндлеры, но соблюдаем очерёдность, это важно!
client.register_handlers_client(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

## For example:
#if message.text == "Привет":
#    await message.answer("И тебе привет!")  # simple reply
# await message.reply(message.text)  # reply to smbdy
# await bot.send_message(message.from_user.id, message.text)  #reply in own branch