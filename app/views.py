import traceback
import app.config as config
import pyautogui
import os
from app.module.motion import touchByPhoto, touchByPos,getPos, getMultiplePos,isPhotoExist, copePaste, typeWrite
from app.module.func import getTime, messageBox
from app.module.res import Res
from time import sleep
from func.db.model.account import selectAllUsers
import eel
import subprocess
import cv2

main_path = config.main['path']

pyautogui.FAILSAFE = False


# 實作手機登入 & 分別取得登入按鈕的入口(座標)
def preLogin(mode, mobile=None, password=None, coordinate=None):
    # os.startfile(config.main['path'])
    # subprocess.Popen(config.main['path'])'
    os.system(f'start /d "C:\Program Files (x86)\XinStars\\" XinUpdate.exe')
    
    touchByPhoto(imagePath=config.getImage(img='login'))
    touchByPhoto(imagePath=config.getImage(img='new_confirm'))
    if mode == 'mobile':
        touchByPhoto(imagePath=config.getImage(mode='mobile', img='item1'))
        touchByPhoto(imagePath=config.getImage(mode='mobile', img='mobile_field'))
        copePaste(mobile)
        # touchByPhoto(imagePath=config.getImage(mode='mobile', img='confirm1'))
        touchByPhoto(imagePath=config.getImage(mode='mobile', img='confirmpwd'))
        touchByPhoto(imagePath=config.getImage(mode='mobile', img='password_field'))
        copePaste(password)
        touchByPhoto(imagePath=config.getImage(mode='mobile', img='confirm2'))
        touchByPhoto(imagePath=config.getImage(mode='mobile', img='item2'))
    elif mode == 'molo':
        touchByPhoto(imagePath=config.getImage(mode='molo', img='item1'))
        touchByPhoto(imagePath=config.getImage(mode='molo', img='mobile_field'), duration=3,confidence=0.9)
        copePaste(mobile)
        touchByPhoto(imagePath=config.getImage(mode='molo', img='password_field'), duration=3)
        typeWrite(password)
        touchByPhoto(imagePath=config.getImage(mode='molo', img='login'),confidence=0.9)
        # touchByPhoto(imagePath=config.getImage(mode='mobile', img='item2'))
    sleep(10)
    if not coordinate:
        coordinates = getMultiplePos(imagePath=config.getImage(mode='mobile', img='login'), confidence=0.95)
        print(f'總共找到:{str(len(coordinates))}個座標')
        coordinates = coordinates[::-1][::-1]
        count = 1
        for coordinate in coordinates:
            x, y, c, d = coordinate
            print(f'點擊 x:{x} y:{y}')
            #eel.consoleLog(f'登入 \n 帳號:{mobile} \n 登入方式:{mode}\n 第{ str(count) }隻角色')
            if coordinate != coordinates[0]:
                preLogin(mode, mobile, password, coordinate)
            doLogin(coordinate)
            count += 1
    else:
        return
    # messageBox('結束程式', '確認')

# 實作 點擊登入按鈕(座標) & 進大廳關閉公告等
def doLogin(coordinate):
    touchByPhoto(imagePath=config.getImage(img='ss'))
    while True:
        touchByPos(coordinate,clicks=2,interval=1)
        sleep(1)
        # 已登入
        if not isPhotoExist(imagePath=config.getImage(img='warn1')):
            #eel.consoleLog(f'沒有被強制退出')
            print(getTime() +'沒有被強制退出')
            break
        #eel.consoleLog(f'被強制退出 等30秒')
        print(getTime() +'被強制退出 等30秒')
        sleep(30)
        touchByPhoto(imagePath=config.getImage(img='confirm1'))

    # 必須用 judge_multi_com 來判斷 是否可以已進入遊戲 以利於多機判斷
    while True:
        flag = isPhotoExist(imagePath=config.getImage(img='judge_multi_com'))
        if flag:
            #eel.consoleLog(f'找到 judge_multi_com 了')
            print(getTime() +'找到 judge_multi_com 了')
            break
        #eel.consoleLog(f'還沒找到 judge_multi_com')
        print(getTime() +'還沒找到 judge_multi_com')
        sleep(1)


    if isPhotoExist(imagePath=config.getImage(img='check')):
        touchByPhoto(imagePath=config.getImage(img='confirm1'))
    else:
        print('沒有多機公告')

    if isPhotoExist(imagePath=config.getImage(img='tmp1')):
        touchByPhoto(imagePath=config.getImage(img='tmp1'))

    if isPhotoExist(imagePath=config.getImage(img='agree')):
        touchByPhoto(imagePath=config.getImage(img='agree'))

    touchByPhoto(imagePath=config.getImage(img='close'))
    return


def start_auto_control(mode=None):
    r = Res()
    try:
        r.changeRes(1600, 900)
        users = selectAllUsers()
        for user in users:
            id = user[0]
            username = user[1]
            password = user[2]
            mobile = int(user[3])
            #eel.consoleLog(f'登入 帳號:{username}')
            if mode!='molo':
                if mobile:
                    #eel.consoleLog(f'登入方式:立即玩')
                    preLogin('mobile', username, password)
                    #eel.consoleLog(f'登入完成')

            molo = int(user[4])
            if mode!='mobile':
                if molo:
                    #eel.consoleLog(f'登入方式:MOLO')
                    preLogin('molo', username, password)
                    #eel.consoleLog(f'登入完成')
        #eel.consoleLog(f'程式已結束運行')
        r.reductRes()
    except:
        traceback.print_exc()
        r.reductRes()