# -*- coding: UTF-8 -*-
import zapytania
import pymysql
import condb
import os
connPar = pymysql.connect(condb.getInfo("host"), condb.getInfo('user'), condb.getInfo('password'), condb.getInfo('database'))

def showMainMenu(userGroup):
    if userGroup == 1:
        m = {1: "Menu Administratora", 2:"Pokaż drzewka", 3:"Zawodnicy", 4:"Koniec"}
        for i in m:
            print("[", i, "]", m[i])


def menuChoice():
    ch= input("Wybierz pozycje menu: ")
    return ch

def showMenuAdmin():
    os.system('cls')
    print("##########   Menu Administratora   ###############")
    menu={2:"Zarządzanie zawodami", 1:"Zgłoszeni zawodnicy w podziale na kategorie", 3:"Rozrysuj drzewka", 4:"Powrót do menu głównego"}
    j = 1
    for i in menu:
        print("[",j,"]",menu[i])
        j +=1
   # menuAdmin()
    
def menuAdmin():
    
    check_test1 =0
    while check_test1 != '4':
        showMenuAdmin()
        choice = menuChoice()
        if choice == '1':
            pass
        elif choice == '2':
            zapytania.qNumberInCat(connPar)
            return True
        elif choice == '3':
            pass
        elif choice == '4':
            return True
        else:
            print("Nieprawidłowy wybór")

#def showCatWeightComp(): # pokazuje ilość zaowników w wagach w danej kategorii
    #ch2 = str(menuChoice())
    #zapytania.qCatWeightComp(ch2)
    
def menuNumberInCat():
    menu = {1:"Rozbicie na kategorie wagowe", 2:"Powrót do menu głównego"}
    j = 1
    for i in menu:
        print("[",j,"]",menu[i])
        j +=1
    choice_test2 = 0
    while choice_test2 != 2:
        choice = menuChoice()
        if choice == '1':
            zapytania.qPlayersInWeightCat(connPar)
            return True
        elif choice == '2':
            choice_test2 = 2
            return choice_test2
        else:
            print("Wybór nieprawidłowy")
            return False
    return True