from app.views import start_auto_control
import os
import traceback
try:
    start_auto_control(mode='mobile')
except:
    traceback.print_exc()
    os.system('.\del.bat')