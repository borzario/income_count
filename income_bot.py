from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

import control_info
import data_base

storage = MemoryStorage()
bot = Bot(token=control_info.TOKEN)
dp = Dispatcher(storage=storage)


from hand import *


def on_startup():
    data_base.db_start()
    print("It is life")


if __name__ == "__main__":
    on_startup()
    dp.run_polling(bot)

