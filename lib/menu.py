# -*- coding: UTF-8 -*-
import os
import pymysql
import condb
import zapytania
connPar = pymysql.connect(condb.getInfo("host"), condb.getInfo('user'), condb.getInfo('password'), condb.getInfo('database'))

def menuChoice():
    ch= int(input("Wybierz pozycje menu: "))
    return ch

def showMainMenu(userGroup):
    if userGroup == 1:
        m = {1: "Menu Administratora", 2:"Pokaż drzewka", 3:"Zawodnicy", 4:"Koniec"}
        for i in m:
            print("[", i, "]", m[i])
            
def showMenuAdmin():
    os.system('cls')
    print("##########   Menu Administratora   ###############")
    menu={1:"Zgłoszeni zawodnicy w podziale na kategorie", 2:"Zarządzanie zawodami", 3:"Rozrysuj drzewka", 4:"Powrót do menu głównego"}
    j = 1
    for i in menu:
        print("[",j,"]",menu[i])
        j +=1


def menuAdmin():
    statusmA = 0
    while statusmA != 99:
        showMenuAdmin()
        choice = menuChoice()
        if choice == 1:
            menuqNumberInCat()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            break
        else:
            print("Nieprawidłowy wybór")
            
def menuqNumberInCat():
    statusqNIC = 0
    while statusqNIC != 99:
        zapytania.qNumberInCat(connPar)
        choiceqNIC = menuChoice()
        if choiceqNIC == 1:
            pass
        elif choiceqNIC == 2:
            break
        else:
            print("Nieprawidłowy wybór")