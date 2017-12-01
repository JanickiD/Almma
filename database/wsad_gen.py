# -*- coding: UTF-8 -*-
import random

class gen:
    __imiona = ("Antoni", "Jakub", "Szymon", "Jan", "Filip", "Franciszek", "Mikołaj", "Aleksander", "Kacper", "Wojciech", "Adam", "Michał", "Marcel", "Wiktor", "Piotr", "Stanisław", "Bartosz", "Mateusz", "Igor", "Nikodem", "Alan", "Leon", "Oliwier", "Maksymilian", "Miłosz", "Dawid", "Tymon", "Oskar", "Karol", "Maciej", "Tomasz", "Ignacy", "Dominik", "Tymoteusz", "Fabian", "Natan", "Krzysztof", "Julian", "Paweł", "Hubert", "Gabriel", "Patryk", "Ksawery", "Kamil", "Bartłomiej", "Sebastian", "Adrian", "Olaf", "Krystian", "Kuba", "Borys")
    __nazwiska = ("Adamczyk", "Dudek", "Górski", "Jabłoński", "Jaworski", "Król", "Majewski", "Malinowski", "Michalski", "Nowakowski", "Nowicki", "Olszewski", "Pawlak", "Pawłowski", "Stępień", "Walczak ", "Wieczorek", "Witkowski", "Wróbel", "Zając", "Baran", "Bąk", "Chmielewski ", "Duda", "Jakubowski", "Jasiński", "Marciniak", "Michalak", "Ostrowski", "Pietrzak", "Rutkowski", "Sadowski", "Sikora", "Szewczyk", "Tomaszewski", "Wilk", "Włodarczyk", "Wróblewski", "Zalewski", "Zawadzki", "Nowak", "Kowalski", "Wiśniewski", "Wójcik", "Kowalczyk", "Kamiński", "Lewandowski", "Zieliński", "Szymański", "Woźniak", "Dąbrowski", "Kozłowski", "Jankowski", "Mazur", "Wojciechowski", "Kwiatkowski", "Krawczyk", "Kaczmarek", "Piotrowski", "Grabowski", "Borkowski", "Czarnecki", "Głowacki", "Kalinowski", "Kaźmierczak", "Kołodziej", "Konieczny", "Kubiak", "Kucharski", "Lis", "Maciejewski", "Mazurek", "Sawicki", "Sikorski ", "Sobczak", "Sokołowski", "Szczepański", "Urbański", "Wasilewski", "Wysocki", "Adamski", "Baranowski", "Błaszyk", "Borowski", "Brzeziński", "Chojnacki", "Gajewski", "Górecki", "Kaczmarczyk", "Kania ", "Krajewski", "Krupa", "Laskowski", "Makowski", "Mróz", "Przybylski", "Szulc", "Szymczak", "Zakrzewski", "Ziółkowski")
    def __init__(self):
        pass
    
    def genImie(self):
        wylosowane_imie = self.__imiona[random.randint(0, len(self.__imiona))]
        return wylosowane_imie
    def genNazwisko(self):
        wylosowane_nazwisko = self.__nazwiska[random.randint(0, len(self.__nazwiska))]
        return wylosowane_nazwisko
    def genWaga(self):
        waga = random.randint(1,8)
        return waga
    def genKategoria(self):
        kategoria = random.randint(1,8)
    
generator = gen()

F=open("wsad.txt", "w")
F.seek(0)
F.writelines(["INSERT INTO `almma`.`player` (`id_p`,`name_p`, `last_name_p`, `id_weight`, `id_club`, `id_cat`) VALUES ('deafult', '"+str(generator.genImie())+"'"+str(generator.genNazwisko())"', '"+str(generator.genWaga())+"', '" + str(generator.genKategoria())+"'"])

#F. INSERT INTO `almma`.`player` (`id_p`,`name_p`, `last_name_p`, `id_weight`, `id_club`, `id_cat`, `id_weight`, `id_weight`) VALUES ('deafult', 'Junior', 'J');

