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
            c.execute("select login from user")
            loginy = c.fetchall()
            
            for i in range(len(loginy)):
                a = loginy[i]
                if login in a:
                    login_status +=1
                    return login
                elif login not in a:
                    print("niepoprawny login")
                    break
            
        
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