from random import randint
import sqlite3


def buildExpression():
    left_op = randint(0, 12)
    right_op = randint(0, 12)

    expression = f'{left_op} x {right_op}: '
    return left_op, right_op, expression


def createTable():
    conn = sqlite3.connect('gamedata.db')
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS gamedata 
    (sessionDate TEXT,
    sessionTime TEXT,
    CorrectCount INTEGER,
    IncorrectCount INTEGER)
    """)

    conn.commit()
    conn.close()


def insertValue(cCount, iCount):
    conn = sqlite3.connect('gamedata.db')
    c = conn.cursor()
    q = f"INSERT INTO gamedata VALUES (date(), time(), {cCount}, {iCount})"
    c.execute(q)
    conn.commit()
    conn.close()
