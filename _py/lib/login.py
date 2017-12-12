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
while check_test != '3':
    menu.showMainMenu(logowanie.getUG())
    choice = menu.menuChoice()
    if choice == '1':
        menu.showMenuAdmin()       
    elif choice == '2':
        pass #wstawić metodę
    elif choice == '3':
        break
    else:
        print("Wybór nieprawidłowy.")

