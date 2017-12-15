# -*- coding: UTF-8 -*-
import sys
sys.path.append('C:\\Users\\user\\Dysk Google\\Reactor\\Almma\\_py\\lib')
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
        lib.menu.menuShowGameTrees()
    if choice == 3:
        pass
    if choice == 4:
        sys.exit()
