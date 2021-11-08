import sqlite3
import numpy as np
import pandas as pd

class Data:

    # db => 'database_example.db'
    def make_conn(self, db):
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        return cur

    def exec_sql(self, cur, sql):
        cur.execute(sql)
        cols = [column[0] for column in cur.description]
        data = np.array([cols])
        print(data)

        rows = cur.fetchall()
        rows = np.array(rows)
        print(rows)
        return data

    def parsing_buildprop(self, db):
        pass

    def parsing_contacts(self, db):
        pass

    def parsing_calllog(self, db):
        pass

    def parsing_mms(self, db):
        pass

    def parsing_calendar(self, db):
        pass




