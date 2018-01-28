#*-* coding: UTF8 *-*
import pymysql
import condb
import os
import menu
import time
import sys
sys.path.append('C:\\Users\\user\\Dysk Google\\Almma\_py')

class Fight:
    counter = 0
    __winnerTab = {1:17, 2:18, 3:19, 4:20, 5:21, 6:22, 7:23, 8:24, 9:25, 10:26, 11:27, 12:28, 13:31, 14:32 }
    
    def __init__(self):
        Fight.setCounter()
    
    def getWinnerTab(fight_id):
        return Fight.__winnerTab.get(fight_id)
    
    def getFightCounterFromDB():
        c = menu.setConnection().cursor()
        c.execute("select max(fightNo) from game_tree")
        for i in c.fetchall():
            fightNo = i[0]
            if fightNo is None:
                return fightNo
            if fightNo is not None:
                return int(fightNo)

    def increaseCounter():
        if Fight.counter is not None:
            Fight.counter += 1
        
    def getCounter():
        return Fight.counter
    
    def setCounter():
        if Fight.counter == 0:
            zbazy = str(Fight.getFightCounterFromDB());
            if zbazy == "None":
                Fight.counter = 1        
            if zbazy != "None":
                Fight.counter = Fight.getFightCounterFromDB()
        if Fight.counter != 0:
            Fight.counter = Fight.getFightCounterFromDB()
        
    
    def fightList():
        red = "r"
        blue = "b"
        c = menu.setConnection().cursor()
        c2 = menu.setConnection().cursor()
        c.execute("select id_cat from category")
        c2.execute("select id_weight from weight_cat")
        categories = c.fetchall()
        weights = c2.fetchall()
        for i in categories:
            category = i[0]
            for j in weights:
                weight = j[0]
                for k in range(1,16):
                    c.execute("select f.id_fight from fight as f join game_tree as gt on f.id_gt_red = gt.id_gt where gt.played != 1 and gt.id_cat = "+str(category)+" and gt.id_weight_cat = "+str(weight)+" order by f.id_fight asc;")
                    c2.execute("select f.id_fight from fight as f join game_tree as gt on f.id_gt_blue = gt.id_gt where gt.played != 1 and gt.id_cat = "+str(category)+" and gt.id_weight_cat = "+str(weight)+" order by f.id_fight asc;")
                    for l in c.fetchall():
                        if str(l[0]) == str(k):
                            red = l[0]
                    for m in c2.fetchall():
                        if str(m[0]) == str(k):
                            blue = m[0]
                    if str(blue) == str(red):
                        Fight.doFight(category, weight, k )
                
                #print("kat: " + str(category) + "|| waga: " + str(weight))
                #if c.rowcount != 0:
                    #for i in c.fetchall():
                        #if i[0] is None:
                            #print("i[0] is None")
                        #elif i[0] is not None:
                            #print("i[0] is not None")
                #elif c.rowcount == 0:
                    #print("liczba walk 0")

                
                #for k in c.fetchall():
                    #print(k)
                    #if k is None:
                        #print("zbiór pusty")
                        #fight_id = k[0]
                        #print(fight_id)
                        #Fight.doFight(category, weight, fight_id)
                    #else:
                        #print("KURWA MAĆ!")
            
    
    def doFight(category, weight, fight_id):
        Fight.setCounter()
        c = menu.setConnection().cursor()
        redPlayer = Fight.getPlayer(fight_id, "r", category, weight)
        bluePlayer = Fight.getPlayer(fight_id, "b", category, weight)
        if redPlayer != None:
            if bluePlayer != None:
                os.system('cls')
                #Fight.increaseCounter()
                print("Walka nr: %3s        Kategoria: %3s         Waga: %3s " % (Fight.getCounter(), category, weight))
                print()
                print("# %25s #        vs        # %25s #" %("Czerwony", "Niebieski" ))
                print("# %25s #                  # %25s #" %(redPlayer, bluePlayer ))
                print()
                Fight.countdown(2)
                print()
                wynik = {1:"Czerwony", 9:"Niebieski"}
                menu.showMenu(wynik)
                while True:
                    result = input("Wskaż zwycięzce:")
                    if result == "1":
                        win = "r"
                        los = "b"
                        break
                    elif result == "9":
                        win = "b"
                        los = "r"
                        break
                    else:
                        print("Wybór niepoprawny!")
                    
                #win = input("Zwycięża: (wpisz R / B)")
                #win = win.lower()
                #los = ""
                #if win == "r":
                    #los = "b"
                #elif win == "b":
                    #los = "r"
                    
                print(win)
                print(los)
                winner = Fight.getIdPlayer(fight_id, win, category, weight)
                loser = Fight.getIdPlayer(fight_id, los, category, weight)
                print("wygrany id" + str(winner))
                print("przegrany id" + str(loser))
                #try:
                #c.execute("INSERT INTO `almma`.`game_tree` (`id_p`, `id_gt`, `id_cat`, `id_weight_cat`) VALUES ('"+str(winner)+"', '"+str(Fight.getWinnerTab(fight_id))+"', '"+str(category)+"', '"+str(weight)+"');")
                c.execute("UPDATE `almma`.`game_tree` SET `played`='1' WHERE id_p = "+str(winner)+"  and id_cat = "+str(category)+" and id_weight_cat = "+str(weight)+";")
                c.execute("UPDATE `almma`.`game_tree` SET `played`='1' WHERE id_p = "+str(loser)+"  and id_cat = "+str(category)+" and id_weight_cat = "+str(weight)+";")
                c.execute("UPDATE `almma`.`game_tree` SET `fightNo`='"+str(Fight.getCounter())+"' WHERE id_p = "+str(winner)+"  and id_cat = "+str(category)+" and id_weight_cat = "+str(weight)+";")
                c.execute("UPDATE `almma`.`game_tree` SET `fightNo`='"+str(Fight.getCounter())+"' WHERE id_p = "+str(loser)+"  and id_cat = "+str(category)+" and id_weight_cat = "+str(weight)+";")                
                #except Exception:
                    #print ("Dodawanie nieudane")
                Fight.increaseCounter()

    def getPlayer(fight_id, color, category, weight):
        if color == "r":
            color = "red"
        elif color == "b":
            color = "blue"
        else:
            print("color error!")
        c = menu.setConnection().cursor()
        qry = 'select (select concat_ws(" ", p.name_p, p.last_name_p) from almma.player as p join almma.game_tree as gt on p.id_p=gt.id_p where id_gt = fight.id_gt_'+str(color)+' and gt.id_cat = '+str(category)+' and gt.id_weight_cat = '+str(weight)+') as blue from almma.fight where id_fight = '+str(fight_id)
        c.execute(qry)
        p = c.fetchall()
        for i in p:
            return i[0]
        
    def getIdPlayer(fight_id, color, category, weight):
        if color == "r":
            color = "red"
        elif color == "b":
            color = "blue"
        c = menu.setConnection().cursor()
        qry = "select (select p.id_p from almma.player as p join almma.game_tree as gt on p.id_p=gt.id_p where gt.id_gt = almma.fight.id_gt_"+str(color)+" and gt.id_cat = "+str(category)+" and gt.id_weight_cat = "+str(weight)+") as blue from almma.fight where id_fight = "+str(fight_id)+";"
        c.execute(qry)
        #c.execute("select (select p.id_p from almma.player as p join almma.game_tree as gt on p.id_p=gt.id_p where gt.id_gt = almma.fight.id_gt_"+str(color)+" and gt.id_cat = "+str(category)+" and gt.id_weight_cat = "+str(weight)+") as blue from almma.fight where id_fight = "+str(fight_id)+";")
        p = c.fetchone()
        for i in p:
            return i    
        
    def countdown(t):
        #t *= 60
        while t:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            t -= 1
        print('Koniec!')    
        

