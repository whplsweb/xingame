import os
import datetime
from func.db.model.task import selectAllTasks
def reboot_reservation(reserved_time):
    current_time = datetime.datetime.now()
    r_hour = int(reserved_time.split(':')[0])
    c_hour = datetime.datetime.now().hour
    if c_hour > r_hour:
        current_time += datetime.timedelta(days=1)
    reserved_time = datetime.datetime.strptime(f"{current_time.strftime('%Y-%m-%d')} {reserved_time}","%Y-%m-%d %H:%M")
    time_interval_sec = int((reserved_time - datetime.datetime.now()).total_seconds())
    cmd = f'shutdown -s -t {time_interval_sec}'
    print(cmd)
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
