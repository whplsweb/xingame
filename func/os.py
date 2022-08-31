import os
import datetime
from func.db.model.task import selectAllTasks
def reboot_reservation(reserved_time):
    current_time = datetime.datetime.now()
    reserved_time = datetime.datetime.strptime(f"{current_time.strftime('%Y-%m-%d')} {reserved_time}","%Y-%m-%d %H:%M")
    
    time_interval_sec = int((reserved_time - current_time).total_seconds())
    if time_interval_sec < 0:
        current_time = current_time + datetime.timedelta(days=1)
        time_interval_sec = int((current_time - reserved_time).total_seconds())

    cmd = f'shutdown -s -t {time_interval_sec}'
    os.system(cmd)

def reboot_cancel():
    cmd = 'shutdown -a'
    os.system(cmd)

def reboot_init():
    tasks = selectAllTasks()
    for task in tasks:
        time = task[1]
        reboot_reservation(time)

def getUserOS():
    if os.name == 'nt':
        return 'Windows'
    elif os.name == 'posix' or os.name == 'darwin':
        return 'Mac'
