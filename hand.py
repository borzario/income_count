import datetime

from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

import data_base
import markups
from aiogram import F
from income_bot import bot, dp
from aiogram.types import Message, CallbackQuery


@dp.message(lambda message: "start" in message.text)
async def start_talking(message: Message):
    await bot.send_message(message.from_user.id, "Что требуется?",
                           reply_markup=markups.ikb_main)


class Income(StatesGroup):
    type_of_income = State()
    how_much = State()


@dp.callback_query(F.data == "add_income")
async def add_income(cb: CallbackQuery, state: FSMContext):
    await bot.send_message(cb.from_user.id, "What type?",
                           reply_markup=markups.ikb_types_of_income)
    await state.set_state(Income.type_of_income)


@dp.callback_query(StateFilter(Income.type_of_income))
async def choose_income(cb: CallbackQuery, state: FSMContext):
    await state.update_data(type=cb.data)
    await bot.send_message(cb.from_user.id, "how much")
    await state.set_state(Income.how_much)

@dp.message(StateFilter(Income.how_much))
async def choose_how_much(message: Message, state: FSMContext):
    await state.update_data(money=int(message.text))
    await state.update_data(today=datetime.datetime.today())
    data = await state.get_data()
    await data_base.put_info_to_base(data)
    await bot.send_message(message.from_user.id, "Done", reply_markup=markups.ikb_main)
    await state.clear()


