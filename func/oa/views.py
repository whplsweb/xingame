import requests
import json



def oa_login(key):
    return True
    url = "https://oa.anlab.cc/api/v1/login"

    payload = {
        'service_name': 'game_bot',
        'key': key
    }

    response = requests.request("POST", url, data=payload)

    res = json.loads(response.text)
    code = int(res['code'])
    msg = res['msg']

    # 驗證正確
    if code:
        return True

    # 驗證失敗
    else:
        return False
