from typing import Optional, Dict, Any

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert

from aiogram.fsm.storage.base import BaseStorage, StorageKey, StateType

from engine import engine
from models import User, Context


class PGSQLStorage(BaseStorage):
    def __init__(self, sqlalchemy_engine: str) -> None:
        self.engine = sqlalchemy_engine
    
    async def set_state(self, key: StorageKey, state: StateType = None) -> None:
        """
        Set state for specified key

        :param key: storage key
        :param state: new state
        """
        with Session(engine) as session:
            user = session.query(User).filter(
                User.telegram_id == key.user_id
            ).first()
            user.state = state.state
            session.commit()
        

    async def get_state(self, key: StorageKey) -> Optional[str]:
        """
        Get key state

        :param key: storage key
        :return: current state
        """
        with Session(engine) as session:
            user = session.query(User).filter(
                User.telegram_id == key.user_id
            ).first()
        return user and user.state

    async def set_data(self, key: StorageKey, data: Dict[str, Any]) -> None:
        """
        Write data (replace)

        :param key: storage key
        :param data: new data
        """
        with Session(engine) as session:
            session.query(Context).filter(
                Context.telegram_user_id == key.user_id
            ).delete()
            session.commit()

            for key, value in data.items():
                context = Context(
                    telegram_user_id=key.user_id,
                    key=key,
                    value=value
                )
                session.add(context)
            session.commit()

    async def get_data(self, key: StorageKey) -> Dict[str, Any]:
        """
        Get current data for key

        :param key: storage key
        :return: current data
        """
        with Session(engine) as session:
            context_items = session.query(Context).filter(
                Context.telegram_user_id == key.user_id,
            ).all()
        return {item.key: item.value for item in context_items}

    async def update_data(self, key: StorageKey, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update date in the storage for key (like dict.update)

        :param key: storage key
        :param data: partial data
        :return: new data
        """
        with Session(engine) as session:
            for k, v in data.items():
                context_insert = insert(Context).values(
                    telegram_user_id=key.user_id,
                    key=k,
                    value=v
                ).on_conflict_do_update(
                    index_elements=('telegram_user_id', 'key'),
                    set_={
                        'telegram_user_id': key.user_id,
                        'key': k,
                        'value': v
                    }
                )
                session.execute(context_insert)
            
            session.commit()

    async def close(self) -> None:  # pragma: no cover
        """
        Close storage (database connection, file or etc.)
        """
        pass
