import traceback
from func.db.model.task import addTask, selectTask, selectAllTasks, editTask, deleteTask
import eel
import json
from func.os import reboot_reservation, reboot_cancel
@eel.expose
def taskadd(time, type):
    # 檢查是否為空
    if not time or not type:
        return json.dumps({
            'code': 0,
            'msg': '數據不可為空'
        })


    flag = addTask(time, type)
    reboot_reservation(time)

    if flag:
        return json.dumps({
            'code': 1,
            'msg': '新增成功'
        })
    else:
        return json.dumps({
            'code': 0,
            'msg': '新增失敗'
        })

@eel.expose
def taskselect(id):
    try:
        task = selectTask(id=id)
        return json.dumps({
            'code': 1,
            'msg': '查詢成功',
            'task': task
        })
    except:
        traceback.print_exc()
        return json.dumps({
            'code': 0,
            'msg': '查詢失敗'
        })


@eel.expose
def taskselectall():
    try:
        tasks = selectAllTasks()
        return json.dumps({
            'code': 1,
            'msg': '查詢成功',
            'tasks': tasks
        })
    except:
        return json.dumps({
            'code': 0,
            'msg': '查詢失敗'
        })

@eel.expose
def taskdelete(id):
    flag = deleteTask(id)
    reboot_cancel()
    if flag:
        return json.dumps({
            'code': 1,
            'msg': '刪除成功'
        })
    else:
        return json.dumps({
            'code': 0,
            'msg': '刪除失敗'
        })

@eel.expose
def taskedit(id, time, type):
    flag = editTask(id, time, type)
    reboot_cancel()
    reboot_reservation(time)
    if flag:
        return json.dumps({
            'code': 1,
            'msg': '修改成功'
        })
    else:
        return json.dumps({
            'code': 0,
            'msg': '修改失敗'
        })
