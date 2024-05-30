from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

import control_info
from engine import engine
from models import Base

storage = MemoryStorage()
bot = Bot(token=control_info.TOKEN)
dp = Dispatcher(storage=storage)


from hand import *


def on_startup():
    print("It is life")


if __name__ == "__main__":
    on_startup()

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    dp.run_polling(bot)



