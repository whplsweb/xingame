from app.module.motion import isPhotoExist, getMultiplePos, touchByPhoto, move2Photo
import app.config as config
from time import sleep
import pyautogui
if __name__ == "__main__":
    while True:
        if isPhotoExist(imagePath=config.getImage(img='multi_judge'), confidence=.9):
            print('multi mode')
            break
        else:
            print('single mode')
        sleep(1)
    # 最多只會匹配到6個

    xs = getMultiplePos(imagePath=config.getImage(mode='multi', img='1'), confidence=.9)
    coordinates_list = []
    # height = 0
    for x in xs:
        print(x)
        # if not height:
        #     height = int(x[3])
        coordinates_list.append(x)
    counter = len(xs)
    img1 = img2 = pyautogui.screenshot()
    counter = 0
    while True:
        img2 = img1
        img1 = pyautogui.screenshot()
        if img1 == img2 and counter != 0:
            break
        move2Photo(imagePath=config.getImage(mode='multi', img='head'), confidence=.9)
        pyautogui.scroll(-1)
        sleep(3)
        counter+=1
    # while True:
    #     # 單純下移
    #     move2Photo(imagePath=config.getImage(mode='multi', img='head'), confidence=.9)
    #     pyautogui.scroll(-10)
    #     i = 0
    #     while True:
    #         sleep(1)
    #         pyautogui.scroll(-10)
    #         if isPhotoExist(imagePath=config.getImage(mode='multi', img='head'), confidence=.9):
    #             if i == 0:
    #                 exit()
    #             print('已找到')
    #             counter+=1
    #             print(counter)
    #             i=0
    #             break
    #         print('未找到')
    #         pyautogui.scroll(-1)
    #         i+=1