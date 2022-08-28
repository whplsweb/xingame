import sqlite3
import traceback
import os

# path = os.getcwd()+'/../data.db'

path = os.getcwd()+'/data.db'

print(path)

con = sqlite3.connect(path)

cursorObj = con.cursor()

