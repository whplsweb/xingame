import traceback
from func.db.model.account import addUser, editUser, selectUser, selectAllUsers, deleteUser, mimicSearch
import eel
import json

@eel.expose
def useradd(username, password, direct, molo):
    # 檢查是否為空
    if not username or not password:
        return json.dumps({
            'code': 0,
            'msg': '帳號密碼不可為空'
        })

    # 檢查是否有相同username的帳號
    if selectUser(username=username):
        return json.dumps({
            'code': 0,
            'msg': '已有相同用戶'
        })
    flag = addUser(username, password, direct, molo)
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
def userselect(id):
    try:
        user = selectUser(id=id)
        print(user)
        return json.dumps({
            'code': 1,
            'msg': '查詢成功',
            'user': user
        })
    except:
        traceback.print_exc()
        return json.dumps({
            'code': 0,
            'msg': '查詢失敗'
        })

@eel.expose
def userselectall():
    try:
        users = selectAllUsers()
        return json.dumps({
            'code': 1,
            'msg': '查詢成功',
            'users': users
        })
    except:
        return json.dumps({
            'code': 0,
            'msg': '查詢失敗'
        })

@eel.expose
def userdelete(id):
    flag = deleteUser(id)
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
def useredit(id, username, password, direct, molo):
    flag = editUser(id, username, password, direct, molo)
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

@eel.expose
def mimicsearch(username):
    try:
        users = mimicSearch(username)
        return json.dumps({
            'code': 1,
            'msg': '查詢成功',
            'users': users
        })
    except:
        return json.dumps({
            'code': 0,
            'msg': '查詢失敗'
        })