from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TEXT_BUTTON_WRITE_TO_GPT = "Написать высшему разуму"

b_add = InlineKeyboardButton(text="Add income", callback_data="add_income")
b_check = InlineKeyboardButton(text="Check income", callback_data="check_income")
ikb_main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=TEXT_BUTTON_WRITE_TO_GPT, callback_data="cbdata")],
                                                 [b_add], [b_check]])

b_taro = InlineKeyboardButton(text="Taro", callback_data="taro")
b_astro = InlineKeyboardButton(text="Astrologia", callback_data="astro")
b_vosk = InlineKeyboardButton(text="Wax", callback_data="vosk")
b_school = InlineKeyboardButton(text="School", callback_data="school")
b_rep = InlineKeyboardButton(text="Tutoring", callback_data="rep")
b_mutki = InlineKeyboardButton(text="Mutki", callback_data="mutki")
b_rent = InlineKeyboardButton(text="Apartment", callback_data="rent")
ikb_types_of_income = InlineKeyboardMarkup(inline_keyboard=[[b_taro], [b_astro], [b_vosk],
                                                            [b_school], [b_rep], [b_mutki], [b_rent]])

b_month_1 = InlineKeyboardButton(text="Jan", callback_data="1")
b_month_2 = InlineKeyboardButton(text="Feb", callback_data="2")
b_month_3 = InlineKeyboardButton(text="Mar", callback_data="3")
b_month_4 = InlineKeyboardButton(text="Apr", callback_data="4")
b_month_5 = InlineKeyboardButton(text="May", callback_data="5")
b_month_6 = InlineKeyboardButton(text="Jun", callback_data="6")
b_month_7 = InlineKeyboardButton(text="Jul", callback_data="7")
b_month_8 = InlineKeyboardButton(text="Aug", callback_data="8")
b_month_9 = InlineKeyboardButton(text="Sep", callback_data="9")
b_month_10 = InlineKeyboardButton(text="Oct", callback_data="10")
b_month_11 = InlineKeyboardButton(text="Nov", callback_data="11")
b_month_12 = InlineKeyboardButton(text="Dec", callback_data="12")
ikb_month = InlineKeyboardMarkup(inline_keyboard=[[b_month_1, b_month_2, b_month_3],
                                                  [b_month_4, b_month_5, b_month_6],
                                                  [b_month_7, b_month_8, b_month_9],
                                                  [b_month_10, b_month_11, b_month_12]])

b_all = InlineKeyboardButton(text="All", callback_data="all")
ikb_types_of_income_for_get = InlineKeyboardMarkup(inline_keyboard=[[b_all], [b_taro], [b_astro], [b_vosk],
                                                                    [b_school], [b_rep], [b_mutki], [b_rent]])


