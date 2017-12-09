# -*- coding: UTF-8 -*-
import zapytania

def showMainMenu(userGroup):
    if userGroup == 1:
        m = {1: "Manage", 2:"Statsy", 3:"KONIEC"}
        for i in m:
            print("[", i, "]", m[i])
        showCompetitionStats()
    else:
        print("Nie zalogowałeś się!")
        
        

        
def menuChoice():
    ch= input("Wybierz pozycje menu: ")
    return ch

def showCompetitionStats():
    ch1 = str(menuChoice())
    if ch1 == str(1):
        print("############### ILOŚĆ ZAWODNIKÓW W KATEGORIACH #######################")
        zapytania.qNumberInCat()
    
    showCatWeightComp()

def showCatWeightComp(): # pokazuje ilość zaowników w wagach w danej kategorii
    ch2 = str(menuChoice())
    zapytania.qCatWeightComp(ch2)