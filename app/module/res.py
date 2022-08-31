import pyautogui
import os
from time import sleep

class Res():
    def __init__(self):
        self.pre_height, self.pre_width = pyautogui.size()
    def changeRes(self, height, width):
        os.system(f'.\QRes.exe /x:{height} /y:{width}')
    def reductRes(self):
        self.changeRes(self.pre_height, self.pre_width)