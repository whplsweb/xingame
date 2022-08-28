import sqlite3
import traceback
from func.db.model.init import con

def insert(token, expire_time):
    query = f"insert into `sys` (token, expire_time) values('{token}', '{expire_time}');"
    try:
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        print("新增成功")
        return True
    except:
        traceback.print_exc()
        print("新增失敗")
        con.rollback()
        return False
    con.close()
    pass

def select(token):
    query = f'SELECT * from sys WHERE `token` = "{token}";'

    try:
        cur = con.cursor()
        cur.execute(query)
        record = cur.fetchall()
        if not record:
            raise ValueError
        print("查詢成功")
        return record
    except:

        traceback.print_exc()
        print("查詢失敗")
        con.rollback()
        return False
    con.close()
