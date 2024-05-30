from sqlalchemy import (
    Integer, Column, Text, DateTime, ForeignKey,
    BigInteger, UniqueConstraint, Boolean, JSON
)
from sqlalchemy.orm import relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass


class UserAndMessage(Base):
    __tablename__ = 'user_and_message'

    id                    = Column(Integer(),
                                   primary_key=True)
    user_telegram_id      = Column(BigInteger(),
                                   )
    context               = Column(Text())


class User(Base):
    __tablename__ = 'users'

    id                    = Column(Integer(),
                                   primary_key=True)
    telegram_id      = Column(BigInteger(),
                                   )
    state                 = Column(  # Состояние
        Text(),
        nullable=False
    )


"""class Context(Base):
    __tablename__ = 'context'

    id                  = Column(
                            Integer(),
                            primary_key=True
                        )
    telegram_user_id    = Column(
                            BigInteger(),
                            ForeignKey('users.telegram_id')
                        )
    key                 = Column(
                            Text(),
                            nullable=False
                        )
    value               = Column(
                            Text(),
                            nullable=False
                        )

    __table_args__ = (
        UniqueConstraint('telegram_user_id', 'key', name='unique_cotext'),
    )"""