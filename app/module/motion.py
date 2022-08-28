import pyautogui
# import pydirectinput as pyautogui
from time import sleep
import clipboard
from app.module.func import getTime
import eel

# def touchByPhoto(imagePath, delay=None, duration=0, clicks=1, interval=0):
#     # print(imagePath)
#
#     if delay:
#         sleep(delay)
#     while True:
#         coordinate = pyautogui.locateCenterOnScreen(imagePath)
#         if coordinate:
#             #eel.consoleLog(f'找到 {imagePath} 了 立即點擊')
#             break
#         print(getTime() + ' not found')
#         #eel.consoleLog(f'找不到 {imagePath} 等待一秒後重試')
#         sleep(1)
#     x, y = coordinate
#     pyautogui.moveTo(x, y, duration=duration)
#     pyautogui.click(x, y, clicks=clicks, interval=interval)

def touchByPhoto(imagePath, delay=None, duration=0, clicks=1, interval=0, confidence=0.5):
    if delay:
        sleep(delay)
    while True:
        coordinate = pyautogui.locateOnScreen(imagePath, confidence=confidence)
        if coordinate:
            #eel.consoleLog(f'找到 {imagePath} 了 立即點擊')
            break
        print(getTime() + ' not found')
        #eel.consoleLog(f'找不到 {imagePath} 等待一秒後重試')
        sleep(1)
    touchByPos(coordinate)

# def touchByPos(coordinate, delay=None, duration=0, clicks=1, interval=0):
#     if delay:
#         sleep(delay)
#     pyautogui.moveTo(coordinate, duration=duration)
#     pyautogui.click(coordinate, clicks=clicks, interval=interval)
#     #eel.consoleLog(f'點擊座標 {coordinate}')

def touchByPos(coordinate, delay=None, duration=0, clicks=1, interval=0):
    if delay:
        sleep(delay)
    pyautogui.moveTo(coordinate, duration=duration)
    pyautogui.click(coordinate, clicks=clicks, interval=interval)
    #eel.consoleLog(f'點擊座標 {coordinate}')


def getMultiplePos(imagePath, confidence=0.5):
    while True:
        coordinates = list(pyautogui.locateAllOnScreen(imagePath, confidence=confidence, grayscale=False))
        if coordinates:
            #eel.consoleLog(f'找到(多個座標) {imagePath} 了 立即點擊')
            #eel.consoleLog(len(coordinates))
            #eel.consoleLog(coordinates)
            break
        #eel.consoleLog(f'找不到(多個座標) {imagePath} 等待一秒後重試')
        print(getTime() + ' not found')
        sleep(1)
    return coordinates


def isPhotoExist(imagePath):
    # 因為有 judge_multi_com

    # sec = 3
    # #eel.consoleLog(f'先睡{str(3)}秒')
    # sleep(sec)

    # flag = pyautogui.locateOnScreen(imagePath)
    flag = pyautogui.locateOnScreen(imagePath, confidence=0.5)
    if flag:
        #eel.consoleLog(f'存在 {imagePath}')
        return True
    #eel.consoleLog(f'不存在 {imagePath}')
    return False

def typeWrite(word):
    pyautogui.typewrite(word)
    #eel.consoleLog(f'貼上文字')

def copePaste(word):
    clipboard.copy(word)
    pyautogui.hotkey("ctrl", "v")
    #eel.consoleLog(f'貼上文字')

