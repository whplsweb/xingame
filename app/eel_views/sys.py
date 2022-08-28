import traceback
import eel
import json
from func.db.model.sys import insert, select
import random
import string
import hashlib
import datetime

def createToken():
    password = generate_password(16)
    cypher_password = md5_encrypt(password)

    # 得到目前時間
    current_time = datetime.datetime.now()

    # 每一個小時 更新一次授權
    expire_time = (current_time + datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')

    try:
        insert(cypher_password, expire_time)
    except:
        traceback.print_exc()
        return

    return password

@eel.expose
def verifyToken(pass_token):
    try:
        if not pass_token:
            raise ValueError('使用者無回傳Token')

        token = select(md5_encrypt(pass_token))[0]
        expire_time = datetime.datetime.strptime(token[1], '%Y-%m-%d %H:%M:%S')
        if not token:
            raise ValueError('不存在的Token')

        current_time = datetime.datetime.now()
        time_interval = int((current_time - expire_time).total_seconds())

        if time_interval > 0:
            raise ValueError('Token已經過期 重新進行授權')

        return json.dumps({
            'code': 1,
            'msg': '授權取得成功！'
        })
    except:
        traceback.print_exc()
        return json.dumps({
            'code': 0,
            'msg': '您尚未取得該軟體的授權 正在將您導向取得視窗'
        })

def generate_password(n):
        characters = list(string.ascii_letters + string.digits)
        random.shuffle(characters)
        password = []
        for i in range(n):
            password.append(random.choice(characters))
        random.shuffle(password)
        password = "".join(password)
        return password

def md5_encrypt(plain_text):
    hl = hashlib.md5()
    hl.update(plain_text.encode(encoding='utf-8'))
    cypher_text = hl.hexdigest()
    return cypher_text
