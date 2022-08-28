import sqlite3
import traceback
from func.db.model.init import con

def addUser(username, password, direct, molo):
    query = f"insert into `account` (username, password, direct, molo) values('{username}', '{password}', '{direct}', '{molo}');"
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

def selectUser(id=None, username=None):
    if id and username:
        query = f'SELECT * from account WHERE `id` = "{id}" AND `username` = "{username}";'
    elif id:
        query = f'SELECT * from account WHERE `id` = "{id}";'
    elif username:
        query = f'SELECT * from account WHERE `username` = "{username}";'
    else:
        return
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

def selectAllUsers():
    query = f"SELECT * from account;"
    try:
        cur = con.cursor()
        cur.execute(query)
        print("查詢成功")
        record = cur.fetchall()
        return record
    except:
        traceback.print_exc()
        print("查詢失敗")
        con.rollback()
        return False
    con.close()

def mimicSearch(username):
    query = f'SELECT * from account WHERE `username` LIKE "%{username}%";'
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

def editUser(id, username, password, direct, molo):
    query = f'UPDATE `account` \
SET `username`="{username}", `password`="{password}", `direct`="{direct}", `molo`="{molo}" \
WHERE `id`="{id}";'
    try:
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        print("修改成功")
        return True
    except:
        traceback.print_exc()
        print("修改失敗")
        con.rollback()
        return False
    con.close()


def deleteUser(id):
    query = f'DELETE FROM `account` WHERE `id` = "{id}";'
    try:
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        print("刪除成功")
        return True
    except:
        traceback.print_exc()
        print("刪除失敗")
        con.rollback()
        return False
    con.close()