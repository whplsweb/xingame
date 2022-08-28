import eel
from app.eel_views import acconut, task, login, sys
from app.views import start_auto_control
from time import sleep
from func.os import reboot_init

@eel.expose
def start():
    start_auto_control()

def init():
    reboot_init()

if __name__ == '__main__':
    print('主程式啟動中 請稍後......')
    reboot_init()
    eel.init('web')
    eel.start('index.html',
              port=8080)