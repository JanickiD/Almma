# -*- coding: UTF-8 -*-
import pymysql
import getpass
import condb
import menu
import signin
import zapytania
import os


    
            

logowanie = signin.signin()
check_test = 0
while not check_test:
    menu.showMainMenu(logowanie.getUG())
    chmm = menu.menuChoice()
    if chmm == '1':
        menu.showMenuAdmin()       
    elif chmm == '2':
        pass #wstawić metodę
    elif chmm == '3':
        os.sys.exit()
    else:
        print("Wybór nieprawidłowy.")

