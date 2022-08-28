import os
main = {
    'path': "C:\Program Files (x86)\XinStars\XinUpdate.exe"
}

def getImage(img, mode=None):
    path =  os.getcwd()+'/app/var/img/'
    if mode:
        path += mode+'/'
    path += img + '.png'
    return path
# image = {
#     'login': os.getcwd()+'\\..\\var/img/login_bak.png',
#     'mobile': {
#         'item1': os.getcwd()+'\\..\\var/img/mobile/item1_bak.png',
#         'item2': os.getcwd()+'\\..\\var/img/mobile/item2.png',
#         'mobile_field': os.getcwd()+'\\..\\var/img/mobile/mobile_field.png',
#         'password_field': os.getcwd() + '\\..\\var/img/mobile/password_field.png',
#         'confirm1': os.getcwd()+'\\..\\var/img/mobile/confirm1.png',
#         'confirm2': os.getcwd()+'\\..\\var/img/mobile/confirm2.png'
#     }
# }