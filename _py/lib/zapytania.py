# -*- coding: UTF-8 -*-
import pymysql
import condb
conn = pymysql.connect(condb.getInfo("host"), condb.getInfo('user'), condb.getInfo('password'), condb.getInfo('database'))
conn.cursor()

def qNumberInCat():
    conn = pymysql.connect(condb.getInfo("host"), condb.getInfo('user'), condb.getInfo('password'), condb.getInfo('database'))
    c=conn.cursor()    
    c.execute("select count(*) as 'liczba zawodników', category.name_cat as 'Kategoria' from category_has_player join category on category_has_player.category_id_cat = category.id_cat group by category_id_cat;")
    for i in c.fetchall():
        print(i[0],"zawodników. Kategoria:", i[1])
        
def qCatWeightComp(category):
    conn = pymysql.connect(condb.getInfo("host"), condb.getInfo('user'), condb.getInfo('password'), condb.getInfo('database'))
    c=conn.cursor()
    c.execute("select count(id_p), w.value_weight, k.name_cat  from category_has_player join player as p on category_has_player.player_id_p = p.id_p join weight_cat as w on p.id_weight = w.id_weight join category as k on category_has_player.category_id_cat = k.id_cat where category_id_cat = "+ str(category) + " group by p.id_weight;")
    for i in c.fetchall():
        print(i)    