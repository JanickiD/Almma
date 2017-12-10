# -*- coding: UTF-8 -*-
import pymysql
import condb
import os

def qNumberInCat(connectionPar):
    os.system("cls") 
    conn = connectionPar
    c=conn.cursor()    
    c.execute("select count(*) as 'liczba zawodników', category.name_cat as 'Kategoria' from category_has_player join category on category_has_player.category_id_cat = category.id_cat group by category_id_cat;")
    print("############### ILOŚĆ ZAWODNIKÓW W KATEGORIACH #######################")
    j = 1
    for i in c.fetchall():
        print("["+ str(j) +"] Kategoria:", i[1], i[0],"zawodników.")
        j += 1
    input()       
    
def qCatWeightComp(category, connectionPar):
    conn = connectionPar
    c=conn.cursor()
    c.execute("select count(id_p), w.value_weight, k.name_cat  from category_has_player join player as p on category_has_player.player_id_p = p.id_p join weight_cat as w on p.id_weight = w.id_weight join category as k on category_has_player.category_id_cat = k.id_cat where category_id_cat = "+ str(category) + " group by p.id_weight;")
    for i in c.fetchall():
        print(i)
    input() #zatrzymanie konsoli
    
#def setTournament(connectionPar):
    #nazwa = input("Wpisz nazwę zawodów: ")
    #date = input("Podaj datę. RRRR-MM-DD")
    #city = input("Wpisz miasto")
    #rank = input("Ranga zawodów. 0 - AlMMA, 1- Mistrzostwa Polski")
    
    #conn = connectionPar
    #c=conn.cursor()
    #c.execute("insert into tournament (name_tourn, city_tourn, date_tourn, rank_tourn) values ('" + str(nazwa) +"', '" + str(city)+"', '"+str(date)+"', "+rank +");')
    #print("Zawody dodano!")l