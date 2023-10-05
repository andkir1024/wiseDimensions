import sqlite3
conn = sqlite3.connect('DayVinchick.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
    users_id              INTEGER         PRIMARY KEY AUTOINCREMENT,
    id_tg                 BIGINT,
    id_vk                 BIGINT,
    phone                 VARCHAR (30),
    lang                  VARCHAR (2)     DEFAULT 'ru',
    lang_code             VARCHAR (2),
    age                   INTEGER,
    male                  VARCHAR (1),
    love                  VARCHAR (1),
    min_age               INTEGER,
    max_age               INTEGER,
    name                  VARCHAR (50),
    description           TEXT,
    photo1                VARCHAR (150),
    photo2                VARCHAR (150),
    photo3                VARCHAR (150),
    video                 VARCHAR (150),
    instagram             VARCHAR (150),
    reg                   BOOLEAN         DEFAULT (0),
    long                  DECIMAL (5, 50),
    lat                   DECIMAL (5, 50),
    ind                   INT             DEFAULT (0) 
                                          NOT NULL,
    is_search             BOOLEAN         NOT NULL
                                          DEFAULT (True),
    count_of_send_message INTEGER         DEFAULT (0));
""")

# cur.execute("""CREATE TABLE IF NOT EXISTS love(
#     love_id         INTEGER       PRIMARY KEY,
#     from_user       BIGINT,
#     to_user         BIGINT,
#     from_username   VARCHAR (150),
#     from_male       VARCHAR (1),
#     from_phone      VARCHAR (20),
#     from_first_name VARCHAR (150),
#     text            TEXT,
#     video           VARCHAR (150),
#     photo           VARCHAR (150),
#     active          BOOLEAN       DEFAULT (1) 
#                                   NOT NULL""")
conn.commit()

conn.close()

# import asyncio
# import time


# async def fun1(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print('fun1 завершена')


# async def fun2(x):
#     print(x**0.5)
#     await asyncio.sleep(3)
#     print('fun2 завершена')


# async def main():
#     task1 = asyncio.create_task(fun1(4))
#     task2 = asyncio.create_task(fun2(4))

#     await task1
#     await task2


# print(type(fun1))

# print(type(fun1(4)))