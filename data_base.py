import sqlite3 as sq


def db_start() -> None:
    global base, cur
    base = sq.connect("money.db")
    cur = base.cursor()
    if base:
        print("Connected to bd is OK!")
    base.commit()


async def put_info_to_base(data):
    print(data)


