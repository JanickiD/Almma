# -*- coding:UTF8 -*-
import pymysql
import condb
import os
import menu

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
    print(" ")
    print("[ 1 ] Pokaż rozbicie na wagi")
    print("[ 2 ] Powrót")
    
def qPlayersInWeightCat(connectionPar):
    os.system("cls")
    print("############### ZAWODNICY W KATEGORIACH W ROZBICIU NA WAGI #######################")
    conn = connectionPar
    c=conn.cursor()
    categories ={1:"Junior", 2:"PK", 3:"OFS", 4:"FC", 5:"Kadet", 6:"Młodzieżowiec", 7:"NoGi Białe", 8:"NoGi Kolor"}
    for i in range(1,8):
        c.execute("select count(*) as 'Liczba zawodników', weight_cat.value_weight as waga from category_has_player as c join player as p on c.player_id_p = p.id_p join weight_cat on p.id_weight = weight_cat.id_weight where c.category_id_cat =" + str(i) + " group by weight_cat.value_weight;")
        print("=======  " + categories[i] + "  ===========" )
        print("waga \t Liczba zawodników")
        for j in c.fetchall():
            print(j[1], "\t" , j[0])
    print ('===========================================')
    print ("Aby powrócić wciśnij wciśnij dowolną cyfrę")

def qShowAllTournaments(connectionPar):
    os.system('cls')
    print("################ ZAWODY #################")
    conn = connectionPar
    c=conn.cursor()
    c.execute('select t.name_tourn, t.city_tourn, t.date_tourn, r.rank, t.tourn_is_active from tournament as t join rank as r on t.rank_tourn = r.id_rank order by t.date_tourn desc')
    j = 1
    for i in c.fetchall():
        print("[",j,"] Nazwa: ", i[0], "   Miasto: ", i[1], "   Data: ", i[2], "   Ranga: ", i[3], "   Aktywny: ", i[4])
        j +=1
    print("")
    print("[ 1 ] Zamknij zawody ")
    print("[ 2 ] Powrót")

def qshowCategories(connectionPar):
    c=connectionPar.cursor()
    c.execute("select * from category")
    res = c.fetchall()
    for i in res:
        print("[",i[0],"] ",i[1])

def qshowWeights(connectionPar):
    c=connectionPar.cursor()
    c.execute("select * from weight_cat")
    res = c.fetchall()
    for i in res:
        print("[",i[0],"] ",i[1])    

def aCloseTournament(connectionPar):
    choicemCT = str(input("Wpisz dokładną nazwę zawodów które chesz zamknąć"))
    c=connectionPar.cursor()
    try:
        c.execute("UPDATE `almma`.`tournament` SET `tourn_is_active`='0' WHERE `name_tourn`='"+str(choicemCT)+"';")
        connectionPar.commit()
        print("Zamknięto zawody! Nie możesz już ich edytować.")
    except:
        connectionPar.rollback()
    input("Naciśnij przycisk aby powrócić")
    
def iCreateTournament(connectionPar):
    name = str(input("Podaj nazwę zawodów: "))
    city = str(input("Wpisz miasto: "))            
    date = str(input("Wpisz datę w formacie RRRR-MM-DD: "))
    rank = int(input("Podaj rangę zawodów. 1 dla ALMMA, 2 dla Mistrzostw Polski, 3 dla Pucharu Polski: "))
    c=connectionPar.cursor()
    try:
        c.execute("INSERT INTO `almma`.`tournament` (`name_tourn`, `city_tourn`, `date_tourn`, `rank_tourn`) VALUES ('"+str(name)+"', '"+str(city)+"', '"+str(date)+"', '"+str(rank)+"');")
        print("Zawody zdefiniowano poprawne.")
    except:
        connectionPar.rollback()
        print("Dodawanie nieudane. Sprawdź wpisywane dane.")
    input("Wciśnij dowolny przycisk aby powrócić do menu zarządzania zawodami")


def iDraw(connectionPar):
    id_gt = (1,9,13,5,3,11,15,7,2,10,14,6,4,12,16,8)
    c = connectionPar.cursor()
    c2 = connectionPar.cursor()
    try:
        for category in range(1,9):
            for weight_cat in range(1,9):
                c2.execute("SET FOREIGN_KEY_CHECKS = 0")
                c.execute("select id_p from player as p join category_has_player as c on p.id_p = c.player_id_p where c.category_id_cat = "+str(category)+" and p.id_weight = "+str(weight_cat)+" order by id_club;")
                players = c.fetchall()
                j = 0
                for i in players:
                    c2.execute("INSERT INTO `almma`.`game_tree` (`id_p`, `id_gt`) VALUES ( "+str(i[0])+", "+str(id_gt[j])+" );")
                    j += 1
    except:
        print("error") 

def iCreateFights(connetionPar):
    c = connectionPar.cursor()
    c2 = connectionPar.cursor()
    try:
        for category in range(1,9):
            for weight_cat in range(1,9):
                c2.execute("SET FOREIGN_KEY_CHECKS = 0")
                c.execute("select id_p from player as p join category_has_player as c on p.id_p = c.player_id_p where c.category_id_cat = "+str(category)+" and p.id_weight = "+str(weight_cat)+" order by id_club;")
                players = c.fetchall()
                j = 0
                for i in players:
                    c2.execute("INSERT INTO `almma`.`game_tree` (`id_p`, `id_gt`) VALUES ( "+str(i[0])+", "+str(id_gt[j])+" );")
                    j += 1
    except:
        print("error") 
    

def qShowGameTrees(connectionPar, category, weight_cat):
    c=connectionPar.cursor()
    c2=connectionPar.cursor()
    c.execute("select name_cat from category where id_cat ="+str(category))
    c2.execute('select value_weight from weight_cat where id_weight ='+str(weight_cat))
    cat = c.fetchone()
    weight = c2.fetchone()
    print("===== Listę walk dla", cat[0], weight[0], "========")
    print()
    
    

def qFindPlayer(connectionPar, name, secondName):
    c=connectionPar.cursor()
    if name == "":
        c.execute("select p.id_p, p.name_p, p.last_name_p, w.value_weight, c.name_club,(SELECT count(category_id_cat) FROM almma.category_has_player where player_id_p = p.id_p) as 'Liczba formuł' from player as p join club as c on p.id_club=c.id_club join weight_cat as w on p.id_weight=w.id_weight where p.last_name_p = '"+str(secondName)+"' ;")
    elif secondName == "":
        c.execute("select p.id_p, p.name_p, p.last_name_p, w.value_weight, c.name_club, (SELECT count(category_id_cat) FROM almma.category_has_player where player_id_p = p.id_p) as 'Liczba formuł'  from player as p join club as c on p.id_club=c.id_club join weight_cat as w on p.id_weight=w.id_weight where p.name_p = '"+str(name)+"' ;")
    elif name == "" and secondName == "":
        print("Nie wpisałeś danych! ")
    else:
        c.execute("select p.id_p, p.name_p, p.last_name_p, w.value_weight, c.name_club, (SELECT count(category_id_cat) FROM almma.category_has_player where player_id_p = p.id_p) as 'Liczba formuł'  from player as p join club as c on p.id_club=c.id_club join weight_cat as w on p.id_weight=w.id_weight where p.name_p = '"+str(name)+"' and p.last_name_p = '"+str(secondName)+"' ;")
    
    result = c.fetchall()
    print("|%3s|%15s|%25s|%5s|%30s|%12s|" %("ID", "Imię", "Nazwisko", "Waga", "Klub","Liczba Formuł"))
    print("-"*95)
    for i in result:
        print("|%3s|%15s|%25s|%5s|%30s|%12s|" % (i[0], i[1], i[2], i[3],i[4],i[5]))

def qEditedPlayer(connectionPar, id):
    c=connectionPar.cursor()
    c.execute("select p.id_p, p.name_p, p.last_name_p, w.value_weight, c.name_club,(SELECT count(category_id_cat) FROM almma.category_has_player where player_id_p = p.id_p) as 'Liczba formuł' from player as p join club as c on p.id_club=c.id_club join weight_cat as w on p.id_weight=w.id_weight where p.id_p = "+str(id)+" ;")
    result = c.fetchall()
    print("Edytujesz zawodnika:")
    for i in result:
        print("|%3s|%15s|%25s|%5s|%30s|%12s|" % (i[0], i[1], i[2], i[3],i[4],i[5]))
    
    
def uChangePlayerName(connectionPar, id):
    newName = str(input("Podaj nowe imię:"))
    c=connectionPar.cursor()
    c.execute("UPDATE player SET name_p ='"+newName+"' WHERE `id_p`='"+str(id)+"' ")
    print("Imię zaktualizowane")
    
def uChangePlayerLastName(connectionPar, id):
    newLastName = str(input("Podaj nowe nazwisko:"))
    c=connectionPar.cursor()
    c.execute("UPDATE player SET last_name_p ='"+newLastName+"' WHERE `id_p`='"+str(id)+"' ")
    print("Nazwisko zaktualizowane")
    
def uChangeWeightCategory(connectionPar, id):
    c=connectionPar.cursor()
    c2 = connectionPar.cursor()
    c.execute("SELECT * FROM almma.weight_cat;")
    print("Z poniższej listy wybierz ID kategorii do której chcesz przypisać zawodnika.")
    print()
    print("|%3s|%4s|" % ("ID", "Waga"))
    print("-"*7)
    categories = c.fetchall()
    for i in categories:
        print("|%3s|%4s|" % (i[0], i[1]))
    status = 0
    while status != 1:
            choice = int(input("Nowa kagegoria: "))
            if 9< choice < 1:
                print("Niewłaściwy wybór. Jeszcze raz.")
            else:
                break
    c2.execute("UPDATE player SET id_weight="+str(choice)+" WHERE id_p="+str(id)+";")
    print("Edycja zakończona")