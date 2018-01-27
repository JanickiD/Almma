#*-* coding: UTF8 *-*
import pymysql
import condb
import os
import menu
import time



class Fight:
    __counter = 1;
    __winnerTab = {1:17, 2:18, 3:19, 4:20, 5:21, 6:22, 7:23, 8:24, 9:25, 10:26, 11:27, 12:28, 13:31, 14:32 }
    

    
    def __init__(self):
        pass
    
    def getWinnerTab(fight_id):
        return Fight.__winnerTab.get(fight_id)

    def increaseCounter():
        Fight.__counter += 1
        
    def getCounter():
        return Fight.__counter
    
    def fightList():
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
                c.execute("select id_fight from fight where finished = 0 order by id_fight asc;")
                for k in c.fetchall():
                    fight_id = k[0]
                    Fight.doFight(category, weight, fight_id)
            
    
    def doFight(category, weight, fight_id):
        c = menu.setConnection().cursor()
        redPlayer = Fight.getPlayer(fight_id, "r", category, weight)
        bluePlayer = Fight.getPlayer(fight_id, "b", category, weight)
        if redPlayer != None:
            if bluePlayer != None:
                os.system('cls')
                Fight.increaseCounter()
                print("Walka nr: %3s        Kategoria: %3s         Waga: %3s " % (Fight.getCounter(), category, weight))
                print()
                print("# %25s #        vs        # %25s #" %("Czerwony", "Niebieski" ))
                print("# %25s #                  # %25s #" %(redPlayer, bluePlayer ))
                print()
                Fight.countdown(2)
                print()
                win = input("Zwycięża: (wpisz R / B)")
                win = win.lower()
                los = ""
                if win == "red":
                    los = "b"
                elif win == "blue":
                    los = "r"
                print(win)
                print(los)
                winner = Fight.getIdPlayer(fight_id, win, category, weight)
                loser = Fight.getIdPlayer(fight_id, los, category, weight)
                try:
                    c.execute("INSERT INTO `almma`.`game_tree` (`id_p`, `id_gt`, `id_cat`, `id_weight_cat`) VALUES ('"+str(winner)+"', '"+str(Fight.getWinnerTab(fight_id))+"', '"+str(category)+"', '"+str(weight)+"');")
                    c.execute("UPDATE `almma`.`game_tree` SET `played`='1' WHERE id_p = "+str(winner)+" , and id_cat = "+str(category)+" and id_weight_cat = "+str(weight)+";")
                    c.execute("UPDATE `almma`.`game_tree` SET `played`='1' WHERE id_p = "+str(loser)+" , and id_cat = "+str(category)+" and id_weight_cat = "+str(weight)+";")
                except Exception:
                    print ("Dodawanie nieudane")

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
        qry = "select (select p.id_p from almma.player as p join almma.game_tree as gt on p.id_p=gt.id_p where gt.id_gt = almma.fight.id_gt_blue and gt.id_cat = "+str(category)+" and gt.id_weight_cat = "+str(weight)+") as blue from almma.fight where id_fight = "+str(fight_id)+";"
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
        

