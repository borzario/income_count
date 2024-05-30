from typing import List, Any

from sqlalchemy.orm import Session

from engine import engine
from models import UserAndMessage, User
import json


def add_uam(
        telegram_user_id: int,
        context: dict
) -> UserAndMessage:
    dumped_context = json.dumps(context)
    with Session(engine) as session:
        uam = UserAndMessage(
            user_telegram_id=telegram_user_id,
            context=dumped_context
        )
        session.add(uam)
        session.commit()
        session.refresh(uam)
    return uam


def get_context(telegram_user_id: int, ) -> list[dict] | None:
    with Session(engine) as session:
        uams = session.query(UserAndMessage).filter(
            UserAndMessage.user_telegram_id == telegram_user_id,
        ).all()
    if len(uams) == 0:
        return []
    else:
        return [json.loads(i.context) for i in uams]


def add_user(user_telegram_id: int):
    with Session(engine) as session:
        user = User(
            telegram_id=user_telegram_id,
            state="start"
        )
        session.add(user)
        session.commit()
        session.refresh(user)
    return user



