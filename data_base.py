import sqlite3 as sq


def db_start() -> None:
    global base, cur
    base = sq.connect("money.db")
    cur = base.cursor()
    if base:
        print("Connected to bd is OK!")
    base.execute('CREATE TABLE IF NOT EXISTS income(user INTEGER, type_of TEXT, money INTEGER, when_added TEXT)')
    base.commit()


async def put_info_to_base(data: dict):
    cur.execute("INSERT INTO income VALUES (?, ?, ?, ?)", tuple(data.values()))
    base.commit()


async def get_income(data: dict) -> int:
    print(data)
    tobr = cur.execute(f"SELECT * FROM income WHERE user == {data['user']} AND"
                           f" when_added == {data['month']}").fetchall()
    if data['type_of'] == "all":
        money = [i[2] for i in tobr]
    else:
        money = [i[2] for i in tobr if i[1] == data['type_of']]
    return sum(money)
