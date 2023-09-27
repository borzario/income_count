from aiogram import Bot, Dispatcher

import control_info

bot = Bot(token=control_info.TOKEN)
dp = Dispatcher()


if __name__ == "__main__":
    dp.run_polling(bot)

