# -*- coding: UTF-8 -*-
import sys
sys.path.append('C:\\Users\\user\\Dysk Google\\Reactor\\Almma\\_py\\lib')
import pymysql
import getpass
import lib.signin
import lib.menu
import lib.login
import os


    
            

logowanie = lib.signin.signin()
check_test = 0
while check_test != '3':
    lib.menu.showMainMenu(logowanie.getUG())
    choice = lib.menu.menuChoice()
    if choice == '1':
        lib.menu.menuAdmin()
    elif choice == '2':
        pass #wstawić metodę
    elif choice == '3':
        pass
    elif choice == '4':
        break
    else:
        print("Wybór nieprawidłowy.")

