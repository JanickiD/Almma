# -*- coding: UTF-8 -*-
import sys
import os
import pymysql
import condb
import zapytania


def setConnection():
    connPar = pymysql.connect(condb.getInfo("host"), condb.getInfo('user'), condb.getInfo('password'), condb.getInfo('database'), autocommit = True, charset='UTF8')
    return connPar

def showMenu(menu):
    for i in menu:
        print("[", i, "]", menu[i])    
    
    


def menuChoice():
    ch=""
    try:
        ch= int(input("Wybierz pozycje menu: "))
    except:
        print("Możesz wprowadzać tylko cyfry!")
    return ch

def showMainMenu(userGroup):
    os.system('cls')
    print("##########   Menu główne   ###############")
    if userGroup == 1:
        m = {1: "Menu Administratora", 2:"Pokaż listę walk", 3:"Zawodnicy", 4:"Koniec"}
    elif userGroup == 2:
        m = {1:"Pokaż listę walk", 2:"Rozegraj walkę", 3:"Koniec" }
    showMenu(m)
    
    
def showMenuAdmin():
    os.system('cls')
    print("##########   Menu Administratora   ###############")
    menu={1:"Liczba zawodników w kategoriach", 2:"Zarządzanie zawodami", 3:"Rozrysuj drzewka", 4:"Powrót do menu głównego"}
    showMenu(menu)
    
def showMenuTournamentsManagement():
    os.system('cls')
    print('##########   Zarządzanie zawodami   ###############')
    menu = {1:"Pokaż zawody", 2:"Dodaj zawody", 3:"Powrót"}
    showMenu(menu)

def showMenuShowGameTrees():
    os.system('cls')
    print('##########   Pokaż drzewka   ###############')
    print('Wybierz kategorię')
    zapytania.qshowCategories(setConnection())

def showMenuPlayers():
    os.system('cls')
    print('########  Zawodnicy  ############')
    menu = {1:"Przegląd po zawodnikach", 2:"Przegląd po kategoriach", 3:"Przegląd po klubach", 4:"Powrót"}
    showMenu(menu)

def showMenuFindPlayer():
    os.system('cls')
    print('######## Przegląd po zawodnikach  ############')    
    menu = {0:"Znajdź zawodnika",1:"Edytuj zawodnika", 2:"Dodaj zawodnika", 3:"Cofnięcie weryfikacji zawodnika",4:"Pokaż formuły w których walczy" ,5:"Powrót"}
    showMenu(menu)

def showMenuEditPlayer():
    #os.system('cls')
    print('######## Edycja zawodnika  ############')      
    menu = {1:"Edytuj imię", 2:"Edytuj nazwisko", 3:"Zmień kategorię wagową", 4:"Powrót"}
    showMenu(menu)


def showMenuQShowPlayerCategories():
    menu={1:"Dodaj kategorię", 2:"Usuń kategorię", 3:"Powrót"}
    showMenu(menu)

def menuAdmin():
    statusmA = 0
    while statusmA != 99:
        showMenuAdmin()
        choice = menuChoice()
        if choice == 1:
            menuqNumberInCat()
        elif choice == 2:
            menuTournamentsManagement()
        elif choice == 3:
            zapytania.iDraw(setConnection())
        elif choice == 4:
            break
        else:
            print("Nieprawidłowy wybór")
            
def menuqNumberInCat():
    statusqNIC = 0
    while statusqNIC != 99:
        zapytania.qNumberInCat(setConnection())
        choiceqNIC = menuChoice()
        if choiceqNIC == 1:
            menuqPlayersInWeightCat()
        elif choiceqNIC == 2:
            break
        else:
            print("Nieprawidłowy wybór")

def menuqPlayersInWeightCat():
    statusqPIWC = 0
    while statusqPIWC != 99:
        zapytania.qPlayersInWeightCat(setConnection())
        chocieqPIWC = menuChoice()
        if chocieqPIWC != None:
            break
        else:
            print("Nieprawidłowy wybór")
            
def menuTournamentsManagement():
    statusmTM = 0
    while statusmTM != 99:
        showMenuTournamentsManagement()
        choiceTM = menuChoice()
        if choiceTM == 1:
            menuShowAllTournaments()
        elif choiceTM == 2:
            zapytania.iCreateTournament(setConnection())
        elif choiceTM == 3:
            break
        else:
            print("Nieprawidłowy wybór")
            
def menuShowAllTournaments():
    statusmSAT = 0
    while statusmSAT != 99:
        zapytania.qShowAllTournaments(setConnection())
        choicemSAT = menuChoice()
        if choicemSAT == 1:
            zapytania.aCloseTournament(setConnection())
        elif choicemSAT == 2:
            break
        else:
            print("Wybór niepoprawny")

def menuShowGameTrees():
    statusmSGT = 0
    while statusmSGT != 99:
        showMenuShowGameTrees()
        category = menuChoice()
        if 0<category<9:
            statusmGTS2 = 0
            while statusmGTS2 != 99:
                zapytania.qshowWeights(setConnection())
                weight_cat = menuChoice()
                if 0<weight_cat<9:
                    zapytania.qShowGameTrees(setConnection(),category, weight_cat)
                    
                    input("Naciśnij klawisz, żeby powrócić do głównego menu")
                    return weight_cat
                else:
                    print("nieprawidłowy wybór")
            return category
        else:
            print("nieprawidłowy wybór")
    
def menuPlayers():
    statusmP =0
    while statusmP !=99:
        showMenuPlayers()
        action = menuChoice()
        if action == 1:
            menuFindPlayer()
        elif action == 2:
            zapytania.qShowPlayerByCategories(setConnection())
        elif action == 3:
            zapytania.qShowPlayersByClubs(setConnection())
        elif action == 4:
            break
        else:
            print("Wybór niepoprawny")


#def findPlayer():
    #os.system('cls')
    #print("Podaj dane zawodnika któreg chcesz znaleźć:")
    #name = str(input("Imię: "))
    #secondName = str(input("Nazwisko: "))
    #zapytania.qFindPlayer(setConnection(), name, secondName)
    #menuFindPlayer()
    
def menuFindPlayer():
    statusmFP =0
    while statusmFP !=99:
        showMenuFindPlayer()
        action = menuChoice()
        if action == 0:
            zapytania.qFindPlayer(setConnection())
        elif action == 1:
            editPlayer()
        elif action == 2:
            zapytania.iAddNewPlayer(setConnection())
        elif action == 3:
            zapytania.uDisableVerifiedPlayer(setConnection())
        elif action == 4:
            id = input("Podaj ID zawodnika: ")
            menuQShowPlayerCategories(zapytania.qShowPlayerCategories(setConnection(), id))
        elif action == 5:
            break
        else:
            print("Wybór niepoprawny")    

def editPlayer():
    while True:
        id = str(input("Wpisz ID zawodnika którego chcesz edytować. Enter aby wyjść. Wybór: "))
        if id != "":
            zapytania.qEditedPlayer(setConnection(), id)
            showMenuEditPlayer()
            action = menuChoice()
            if action == 1:
                zapytania.uChangePlayerName(setConnection(), id)
            elif action == 2:
                zapytania.uChangePlayerLastName(setConnection(), id)
            elif action == 3:
                zapytania.uChangeWeightCategory(setConnection(), id)
            elif action == 4:
                break
            elif id == "":
                break
            else:
                print("Wybór niepoprawny")    
        else:
            break

def menuQShowPlayerCategories(id):
    while True:
        showMenuQShowPlayerCategories()
        action = menuChoice()
        if action == 1:
            zapytania.iAddPlayerCategory(setConnection(), id)
        elif action == 2:
            zapytania.uDelPlayerCategory(setConnection(), id)
            break
        elif action == 3:
            break
        else: 
            print("Wybór nieprawidłowy")
            

def menuMain(userGroup):
    if userGroup == 1:
        choice = menuChoice()
        if choice == 1:
            menuAdmin()
        if choice == 2:
            menuShowGameTrees()
        if choice == 3:
            menuPlayers()
        if choice == 4:
            sys.exit()   
    elif userGroup == 2:
        choice = menuChoice()
        if choice == 1:
            menuShowGameTrees()
        if choice == 2:
            pass
        if choice == 3:
            sys.exit()  
