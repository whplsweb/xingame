import sqlite3
import traceback
from func.db.model.init import con
def addTask(time, type):
    query = f"insert into `task` (time, type) values('{time}', '{type}');"
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

def selectTask(id=None):
    if id:
        query = f'SELECT * from task WHERE `id` = "{id}";'
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


def selectAllTasks():
    query = f"SELECT * from task;"
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

def editTask(id, time, type):
    query = f'UPDATE `task` \
SET `time`="{time}", `type`="{type}"\
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


def deleteTask(id):
    query = f'DELETE FROM `task` WHERE `id` = "{id}";'
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

if __name__ == "__main__":
    deleteTask(1)