import datetime

from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from gpt import gpt
from income_bot import bot, dp
from aiogram.types import Message, CallbackQuery

from requests_functions import add_user


class WatchIncome(StatesGroup):
    gpt = State()


@dp.message(lambda message: "start" in message.text)
async def start_talking(message: Message, state: FSMContext):
    add_user(message.from_user.id)
    await bot.send_message(message.from_user.id,
                           "Вы перешли в общение с чат гпт. Отправляйте вопросы.")
    await state.set_state(WatchIncome.gpt)


@dp.message(
    StateFilter(WatchIncome.gpt)
)
async def talks(message: Message):
    msg = await bot.send_message(message.from_user.id,
                                 "обрабатывается")
    answer = await gpt(message)
    await bot.edit_message_text(answer, msg.chat.id, msg.message_id, )
