import win32api
import win32con
from datetime import datetime

def getTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def messageBox(title='', msg=''):
    win32api.MessageBox(win32con.NULL, msg, title, win32con.MB_OK)