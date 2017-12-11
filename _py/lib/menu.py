# -*- coding: UTF-8 -*-
import zapytania
import pymysql
import condb
import os
connPar = pymysql.connect(condb.getInfo("host"), condb.getInfo('user'), condb.getInfo('password'), condb.getInfo('database'))

def showMainMenu(userGroup):
    if userGroup == 1:
        m = {1: "Menu Administratora", 2:"Statsy", 3:"KONIEC"}
        for i in m:
            print("[", i, "]", m[i])
        #choice = menuChoice()
        #if str(choice)==1:
            #showMenuAdmin()

def menuChoice():
    ch= input("Wybierz pozycje menu: ")
    return ch

def showMenuAdmin():
    os.system('cls')
    print("##########   Menu Administratora   ###############")
    menu={1:"Zarządzanie zawodami", 2:"Zgłoszeni zawodnicy w podziale na kategorie", 3:"Rozpiski", 4:"Powrót do menu głównego"}
    j = 1
    for i in menu:
        print("[",j,"]",menu[i])
        j +=1
    choice = menuChoice()
    check_test1 =0
    while not check_test1:
        if str(choice) == '2':
            zapytania.qNumberInCat(connPar)
            return True

def showCatWeightComp(): # pokazuje ilość zaowników w wagach w danej kategorii
    ch2 = str(menuChoice())
    zapytania.qCatWeightComp(ch2)
    
def menuNumberInCat():
    menu = {1:"Rozbicie na kategorie wagowe", 2:"Powrót do menu głównego"}
    j = 1
    for i in menu:
        print("[",j,"]",menu[i])
        j +=1
    choice_test2 = 0
    choice = menuChoice()
    while not choice_test2:
        if str(choice) == '1':
            zapytania.qPlayersInWeightCat(connPar)
        if str(choice) == '2':
            return False   