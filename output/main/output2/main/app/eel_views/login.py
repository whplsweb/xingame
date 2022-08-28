import eel
from func.oa.views import oa_login
import json
from app.eel_views.sys import createToken

@eel.expose
def login(key):
    flag = oa_login(key)
    if flag:
        token = createToken()
        return json.dumps({
            'code': 1,
            'msg': '成功取得授權，正在為您導向主程式',
            'token': token
        })
    else:
        return json.dumps({
            'code': 0,
            'msg': '授權取得失敗，請檢查您的授權碼'
        })
