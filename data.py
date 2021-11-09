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

    def close_conn(self, conn):
        conn.close()
        return

    def data_extract_db(self, db, sql):
        conn = sqlite3.connect(db)
        cur = conn.cursor()

        cur.execute(sql)
        cols = [column[0] for column in cur.description]
        data = np.array([cols])
        # print(data)

        rows = cur.fetchall()
        rows = np.array(rows)
        # print(rows)

        data = np.append(data, rows, axis=0)
        print('data_extract_db(' + db + ', ' + sql + ')')
        print(data)

        conn.close()
        return data

    def parsing_text(self, text):
        pass

    def parsing_buildprop(self, file):
        s1, s2, s3, s4 = '', '', '', ''
        os, model, build_id = '', '', ''
        f = open(file, 'r', encoding='utf-8')

        fs = f.readlines()

        for line in fs:
            line = line[:-1].split('=', 2)
            if line[0] == 'net.bt.name':
                s1 = line[1]
            if line[0] == 'ro.build.version.release':
                s2 = line[1]
            if line[0] == 'ro.build.product':
                s3 = line[1]
            if line[0] == 'ro.system.build.id':
                s4 = line[1]

        if not s1 == '':
            os = s1
            if not s2 == '':
                os = os + s2
        if not s3 == '':
            model = s3
        if not s4 == '':
            build_id = s4
        return os, model, build_id


