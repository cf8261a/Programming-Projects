from random import randint
import sqlite3


def buildExpression():
    left_op = randint(0, 12)
    right_op = randint(0, 12)

    expression = f'{left_op} x {right_op}: '
    return left_op, right_op, expression


# def createTable():
#     conn = sqlite3.connect('gamedata.db')
#     c = conn.cursor()

#     c.execute("""
#     CREATE TABLE IF NOT EXISTS gamedata
#     (sessionDate TEXT,
#     sessionTime TEXT,
#     CorrectCount INTEGER,
#     IncorrectCount INTEGER)
#     """)

#     conn.commit()
#     conn.close()


# def insertValue(cCount, iCount):
#     conn = sqlite3.connect('gamedata.db')
#     c = conn.cursor()
#     q = f"INSERT INTO gamedata VALUES (date(), time(), {cCount}, {iCount})"
#     c.execute(q)
#     conn.commit()
#     conn.close()

class BackendDB:

    def createTable(self):
        q = """
        CREATE TABLE IF NOT EXISTS gamedata 
        (sessionDate TEXT,
        sessionTime TEXT,
        CorrectCount INTEGER,
        IncorrectCount INTEGER)
        """
        return q

    def insertValue(self, cCount, iCount):
        """Creates a query to insert values into the existing db"""

        q = f"INSERT INTO gamedata VALUES (date(), time(), {cCount}, {iCount})"
        return q

    def getHighestScore(self):
        q = """SELECT MAX(CorrectCount) FROM gamedata"""
        return q

    def getAvgScore(self):
        q = """SELECT AVG(CorrectCount) FROM gamedata"""
        return q

    def invokeSQLite(self, cCount=None, iCount=None, how=None):
        """Creates a connection to the gamedb"""

        conn = sqlite3.connect('gamedata.db')
        c = conn.cursor()

        if how == 'CREATETABLE':
            query = self.createTable()
        elif how == 'INSERTVALUE':
            query = self.insertValue(cCount, iCount)
        elif how == 'HIGHSCORE':
            query = self.getHighestScore()
        elif how == 'AVGSCORE':
            query = self.getAvgScore()

        c.execute(query)
        rows = c.fetchall()

        conn.commit()
        conn.close()
        if how in ['HIGHSCORE', 'AVGSCORE']:
            return rows[0][0]
