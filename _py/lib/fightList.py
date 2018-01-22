#*-* coding: UTF8 *-*
import pymysql
import condb
import os
import menu
import time
import fight

    
    
def showGameTree(connectionPar, category, weight,):
    def getPlayer(fight_id,color):
        if color == "r":
            color = "red"
        elif color == "b":
            color = "blue"
        else:
            print("color error!")
        c = connectionPar.cursor()
        qry = 'select (select concat_ws(" ", p.name_p, p.last_name_p) from almma.player as p join almma.game_tree as gt on p.id_p=gt.id_p where id_gt = fight.id_gt_'+str(color)+' and gt.id_cat = '+str(category)+' and gt.id_weight_cat = '+str(weight)+') as blue from almma.fight where id_fight = '+str(fight_id)+';'
        c.execute(qry)
        p = c.fetchone()
        for i in p:
            return i
    
    
    
    
    print("%20s ---" % (getPlayer("1", "r")))
    print("%20s   |---%20s" % (" ", getPlayer("9", "r")))
    print("%20s ---   %20s|" % (getPlayer("1", "b"), " "))
    print("%20s       %20s|---%20s" %(" ", " ", getPlayer("13", "r")))        
    print("%20s ---   %20s|   %20s|" % (getPlayer("2", "r"), " ", " "))
    print("%20s   |---%20s    %20s|" % (" ", getPlayer("9", "b"), " "))
    print("%20s ---   %20s    %20s|" % (getPlayer("2", "b"), " ", " "))
    print("%20s       %20s    %20s|---%20s" % (" ", " "," " ,getPlayer("16", "r")))
    print("%20s ---   %20s    %20s|   %20s|" % (getPlayer("3", "r"), " ", " ", " "))
    print("%20s   |---%20s    %20s|   %20s|" % (" ", getPlayer("10", "r"), " ", " "))
    print("%20s ---   %20s|   %20s|   %20s|" % (getPlayer("3", "b"), " ", " ", " "))
    print("%20s       %20s|---%20s    %20s|" %(" ", " ",getPlayer("13", "b") ," "))        
    print("%20s ---   %20s|   %20s    %20s|" % (getPlayer("4", "r"), " ", " ", " "))
    print("%20s   |---%20s    %20s    %20s|" % (" ", getPlayer("10", "b"), " ", " "))
    print("%20s ---   %20s    %20s    %20s|" % (getPlayer("4", "b"), " ", " ", " "))
    print("%20s       %20s    %20s    %20s|---" % (" ", " ", " ", " "))
    print("%20s ---   %20s    %20s    %20s|" % (getPlayer("5", "r"), " ", " ", " "))
    print("%20s   |---%20s    %20s    %20s|" % (" ", getPlayer("11", "r"), " ", " "))
    print("%20s ---   %20s|   %20s    %20s|" % (getPlayer("5", "b"), " ", " ", " "))
    print("%20s       %20s|---%20s    %20s|" %(" ", " ",getPlayer("14", "r") ," "))        
    print("%20s ---   %20s|   %20s|   %20s|" % (getPlayer("6", "r"), " ", " ", " "))
    print("%20s   |---%20s    %20s|   %20s|" % (" ", getPlayer("11", "b"), " "," "))
    print("%20s ---   %20s    %20s|   %20s|" % (getPlayer("6", "b"), " ", " "," "))
    print("%20s       %20s    %20s|---%20s" % (" ", " "," " , getPlayer("16", "b")))
    print("%20s ---   %20s    %20s|" % (getPlayer("7", "r"), " ", " "))
    print("%20s   |---%20s    %20s|" % (" ", getPlayer("12", "r"), " "))
    print("%20s ---   %20s|   %20s|" % (getPlayer("7", "b"), " "," "))
    print("%20s       %20s|---%20s" %(" ", " ", getPlayer("14", "b")))        
    print("%20s ---   %20s| " % (getPlayer("8", "r"), " "))
    print("%20s   |---%20s" % (" ", getPlayer("12", "b")))
    print("%20s ---   %20s" % (getPlayer("8", "b"), " "))
    print()
    print("Walka o III miejsce")
    print()
    print("%20s --- " % (getPlayer("15", "r")))
    print("%20s   |---" % (" "))
    print("%20s --- " % (getPlayer("15", "b")))





