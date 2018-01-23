# -*- coding: UTF-8 -*-
#import sys
#sys.path.append('.lib')
import getpass
import pymysql
import condb




class signin:
    __userGroup = None
    
    def __init__(self):
        self.conn = pymysql.connect(condb.getInfo("host"), condb.getInfo('user'), condb.getInfo('password'), condb.getInfo('database'))
        self.login = self.getLogin()
        self.password = self.getPass()
        
        
    def getLogin(self):
        c = self.conn.cursor()
        login_status = 0
        while login_status == 0:
            login = input("Login:")
            c.execute("select login from user order by login desc")
            loginy = c.fetchall()    
            for i in loginy:
                a = i[0]
                if login == a:
                    login_status +=1
                    return login
                elif login not in a:
                    print("niepoprawny login")
            
        
    def getPass(self):
        c = self.conn.cursor()        
        pass_status = 0
        while pass_status == 0:
            password = getpass.getpass(prompt="Hasło: ")
            c.execute("select pass from user where login='"+str(self.login)+"\'")
            pswrds = c.fetchall()
            
            for i in range(len(pswrds)):
                a = pswrds[i]
                if password in a:
                    pass_status +=1
                    print("Zalogowany!")
                    self.setUserGroup()
                    return password
                elif pswrds not in a:
                    print("Hasło nieprawidłowe")
            
    
    def setUserGroup(self):
        c = self.conn.cursor()
        c.execute("select user_group from user where login='"+str(self.login)+"\'")
        for i in c.fetchone():
            self.__userGroup = i
        
    def getUG(self):
        return self.__userGroup
    
    def getConn(self):
        return self.conn
    
    #def signIn(self):
        #login = input("Podaj login: ")
        #pswd = input("Podaj hasło: ")
        #c = self.conn.cursor()
        #try:
            #c.execute("select login, pass from user")
            #for i in c.fetchall():
                #if login in i[0]:
                    