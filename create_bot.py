# Этот модуль создан для взаимоимпорта, чтобы не было ошибки при переходе между модулями
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
# Импортируем из библиотеки aiogram хранилище для машины состояний
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()



bot = Bot(token=os.getenv('SECRET_TOKEN'))
dp = Dispatcher(bot, storage=storage)