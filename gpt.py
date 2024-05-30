import json

import g4f.models
from aiogram.types import Message
from g4f.client import AsyncClient, Client

from income_bot import bot
from requests_functions import get_context, add_uam


async def gpt(message: Message):
    msgs = get_context(message.from_user.id)
    client = Client()
    temp = True
    while temp:
        i = 0
        models = [model for model in g4f.models._all_models if model[:5] in ("gpt-4", "gpt-4o") or model[:5] == "gpt-3"]
        try:
            j = i % 6
            response = client.chat.completions.create(
                model=models[j],
                messages=msgs + [{"role": "user", "content": message.text}], )

            if response.choices[0].message.content != "当前地区当日额度已消耗完, 请尝试更换网络环境":
                temp = False
            else:
                print("________Китайская хуета")
                client = Client()
        except Exception as err:
            i += 1
            print(err)
            continue

    add_uam(message.from_user.id, {"role": "user", "content": message.text})

    add_uam(message.from_user.id, {"role": response.choices[0].message.role, "content": response.choices[0].message.content})

    return response.choices[0].message.content
