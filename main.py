#*-* coding: UTF8 *-*
import sys
sys.path.append('C:\\Users\\user\\Desktop\\almma\\lib')
import pymysql
import lib.signin
import lib.menu

almma = lib.signin.signin()

status = 0
while status == 0:
    lib.menu.showMainMenu(almma.getUG())
    choice = lib.menu.menuChoice()
    if choice == 1:
        lib.menu.menuAdmin()
    if choice == 2:
        pass
    if choice == 3:
        pass
    if choice == 4:
        sys.exit()