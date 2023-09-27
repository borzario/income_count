from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

b_add = InlineKeyboardButton(text="Add income", callback_data="add_income")
b_check = InlineKeyboardButton(text="Check income", callback_data="check_income")
ikb_main = InlineKeyboardMarkup(inline_keyboard=[[b_add], [b_check]])

b_taro = InlineKeyboardButton(text="Taro", callback_data="taro")
b_astro = InlineKeyboardButton(text="Astrologia", callback_data="astro")
b_vosk = InlineKeyboardButton(text="Wax", callback_data="vosk")
b_school = InlineKeyboardButton(text="School", callback_data="school")
b_mutki = InlineKeyboardButton(text="Mutki", callback_data="mutki")
b_rent = InlineKeyboardButton(text="Apartment", callback_data="rent")
ikb_types_of_income = InlineKeyboardMarkup(inline_keyboard=[[b_taro], [b_astro], [b_vosk],
                                                            [b_school], [b_mutki], [b_rent]])
