# Этот модуль создан для взаимоимпорта, чтобы не было ошибки при переходе между модулями
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os


bot = Bot(token=os.getenv('SECRET_TOKEN'))
dp = Dispatcher(bot)