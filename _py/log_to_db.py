# -*- coding: UTF-8 -*-
import getpass
import pymysql

class con_db:
    
    
    def __init__ (self):
        import package.login_table
        self.__logdata = package.login_table.sl()
        self.__user = None
        #self.__password = self.getPassword()


    def getUser(self):
        status = 0
        while status == 0:
            user = input("Wpisz login: ")
            if user in self.__logdata:
                status = 1
                self.__user = user
            else:
                print("Użytkownik nieprawidłowy. Spróbój jeszcze raz: ")
                status = 0
            
        return user
    
    def getPassword(self):
        status = 0
        while status == 0:
            pswrd = getpass.getpass(prompt="Wpisz hasło: ", stream= None)
            if pswrd == self.__logdata[self.__user]:
                status = 1
            else:
                print("Hasło nieprawidłowe. Spróbój jeszcze raz: ")
                status = 0
            
        return pswrd
    
    def setConn(self):
        connection = pymysql.connect('localhost', self.getUser(), self.getPassword(), 'almma')
        c = connection.cursor()
        return c




    