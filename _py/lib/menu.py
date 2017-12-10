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
    if str(choice) == 2:
        zapytania.qNumberInCat()

def showCatWeightComp(): # pokazuje ilość zaowników w wagach w danej kategorii
    ch2 = str(menuChoice())
    zapytania.qCatWeightComp(ch2)