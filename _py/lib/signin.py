# -*- coding: UTF-8 -*-
import pymysql
import condb
import getpass

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
            c.execute("select login from user")
            loginy = c.fetchall()
            
            for i in range(len(loginy)):
                a = loginy[i]
                if login in a:
                    login_status +=1
                elif login not in a:
                    continue
            return login
        
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
                elif pswrds not in a:
                    print("Hasło nieprawidłowe")
            return password
    
    def setUserGroup(self):
        c = self.conn.cursor()
        c.execute("select user_group from user where login='"+str(self.login)+"\'")
        for i in c.fetchone():
            self.__userGroup = i
        
    def getUG(self):
        return self.__userGroup