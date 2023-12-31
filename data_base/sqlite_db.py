import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur 
    base = sq.connect('pizza_cool.db')
    cur = base.cursor()
    if base:
        print('База данных подключена норм!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message): # Аргумент message используется для отправки в личку
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')

async def sql_read2():
    # Эта функция чтобы прочитать выборку из БД и передать в модуль admin
    return cur.execute('SELECT * FROM menu').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))
    base.commit()
