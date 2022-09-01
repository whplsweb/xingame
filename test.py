from app.views import start_auto_control
import os
try:
    start_auto_control()
except:
    os.system('./del.bat')