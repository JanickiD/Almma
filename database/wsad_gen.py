# -*- coding: UTF-8 -*-
import random

class gen:
    __imiona = ("Antoni", "Jakub", "Szymon", "Jan", "Filip", "Franciszek", "Mikołaj", "Aleksander", "Kacper", "Wojciech", "Adam", "Michał", "Marcel", "Wiktor", "Piotr", "Stanisław", "Bartosz", "Mateusz", "Igor", "Nikodem", "Alan", "Leon", "Oliwier", "Maksymilian", "Miłosz", "Dawid", "Tymon", "Oskar", "Karol", "Maciej", "Tomasz", "Ignacy", "Dominik", "Tymoteusz", "Fabian", "Natan", "Krzysztof", "Julian", "Paweł", "Hubert", "Gabriel", "Patryk", "Ksawery", "Kamil", "Bartłomiej", "Sebastian", "Adrian", "Olaf", "Krystian", "Kuba", "Borys")
    __nazwiska = ("Adamczyk", "Dudek", "Górski", "Jabłoński", "Jaworski", "Król", "Majewski", "Malinowski", "Michalski", "Nowakowski", "Nowicki", "Olszewski", "Pawlak", "Pawłowski", "Stępień", "Walczak ", "Wieczorek", "Witkowski", "Wróbel", "Zając", "Baran", "Bąk", "Chmielewski ", "Duda", "Jakubowski", "Jasiński", "Marciniak", "Michalak", "Ostrowski", "Pietrzak", "Rutkowski", "Sadowski", "Sikora", "Szewczyk", "Tomaszewski", "Wilk", "Włodarczyk", "Wróblewski", "Zalewski", "Zawadzki", "Nowak", "Kowalski", "Wiśniewski", "Wójcik", "Kowalczyk", "Kamiński", "Lewandowski", "Zieliński", "Szymański", "Woźniak", "Dąbrowski", "Kozłowski", "Jankowski", "Mazur", "Wojciechowski", "Kwiatkowski", "Krawczyk", "Kaczmarek", "Piotrowski", "Grabowski", "Borkowski", "Czarnecki", "Głowacki", "Kalinowski", "Kaźmierczak", "Kołodziej", "Konieczny", "Kubiak", "Kucharski", "Lis", "Maciejewski", "Mazurek", "Sawicki", "Sikorski ", "Sobczak", "Sokołowski", "Szczepański", "Urbański", "Wasilewski", "Wysocki", "Adamski", "Baranowski", "Błaszyk", "Borowski", "Brzeziński", "Chojnacki", "Gajewski", "Górecki", "Kaczmarczyk", "Kania ", "Krajewski", "Krupa", "Laskowski", "Makowski", "Mróz", "Przybylski", "Szulc", "Szymczak", "Zakrzewski", "Ziółkowski")
    __kluby = ("Cross Fight Radom", "Octagon Team ", "Spartakus Rzeszów", "DAAS Berserkers Team Bielsko Biała", "Gladio", "Golden Dragon Bydgoszcz ", "Dziki Wschód", "Ankos Zapasy Poznań ", "Brawler Końskie", "GŁD Team Piła", "MMA Czarni Słupsk ", "MKS Kalina Lublin ", "Gold Team Polska", "rio Grappling Club Monster-Rybnik ", "Rio Grappling Ostrów Wlkp", "Contender Kamienna Góra ", "Streffa Fight Team Lubin", "MMA Team Ełk", "SK Kickboxing Kielce", "Ronin Gold Team Koszalin", "Walka Gniezno", "MKS SAMBO CHEŁM ", "Berserker Szczecin ", "BJJ NEXT LEVEL", "KEMPO Bushido- KTJMMA TEAM R	 Arrachion Olsztyn", "Berserkers Team Olsztyn", "Sportowy Białystok Team", "ASW Black Panther Bydgoszcz", "Berserkers Team Kołobrzeg", "MMA Devil Świebodzin", "Nastula Club", "Pride Złotoria", "Silesian Cage Club", "MMA Krosno", "Fight Club Łomża ", "Gracie Barra Łódź", "Academia Gorilla", "Grappler Grudziądz", "MMA Witkowo ", "Niedźwiedzie Stronie Śląskie", "Warszawskie Centrum Atletyki", "Eko Różanka Pankration Team", "Bambero Team Wyszków", "Forca Brava Gold Team Polska", "Copacabana Warszawa", "MMA Devil Poznań", "FightLab Wrocław", "Zenith Głuponie", "Rawski Klub Karate Kyokushin", "Impact Płock", "Fight Club Bytom", "MMATADORES Katowice", "Przemol Boxing Team", "Kaiser Sports Olsztyn", "GKS Górnik Łęczna - MMA", "Fightman", "Fighting X Club", "Copacabana Łódź ", "Szkoła Walki Drwala", "Sihasapa Gold Team", "Legion Team Tarnów", "Hunter MMA", "Halny Nowy Sącz/Sekcja ", "OBAMMA Fight Team", "Black Horse MMA Łomża ", "No Limit Toruń", "Berserkers Venganza Racibórz", "Veto Team Bielsko-Biała ", "Grappling Kraków", "Bastion Tychy", "MKS Lubartów", "Berserkers Team Stargard ", "Fight Academy Bydgoszcz", "Zenith Łódź", "Oświęcimski Klub MMA", "RAPAX MMA Siemianowice", "War Dogs", "B-zone MMA Kędzierzyn-Koźle")
    __x = 0
    def __init__(self):
        pass
    
    def genImie(self):
        wylosowane_imie = self.__imiona[random.randint(0, len(self.__imiona)-1)]
        return wylosowane_imie
    def genNazwisko(self):
        wylosowane_nazwisko = self.__nazwiska[random.randint(0, len(self.__nazwiska)-1)]
        return wylosowane_nazwisko
    def genWaga(self):
        waga = random.randint(1,8)
        return waga
    def genKategoria(self):
        kategoria = random.randint(1,8)
        return kategoria
    
    def genKlub(self):
        klub = random.randint(0, len(self.__kluby)-1)
        return klub
    def ile(self):
        return len(self.__kluby)
    
generator = gen()
print(generator.ile())

C=open("clubs.txt", "w")
C.seek(0)
for i in range(0, generator.ile()-1):
    C.writelines(["\nINSERT INTO `almma`.`club` (`name_club`, `city_club`, `trainer_name`) VALUES('"+str(generator.genKlub())+"', 'daefult', 'daefult');" ])
C.close()
P=open("Players.txt", "w")
P.seek(0)
for i in range (0, 180):
    P.writelines(["INSERT INTO `almma`.`player` (`name_p`, `last_name_p`, `id_weight`, `id_club`, `id_cat`) VALUES ('"+str(generator.genImie())+"', '"+str(generator.genNazwisko())+"', '"+str(generator.genWaga())+"', '" + str(generator.genKategoria())+"', '"+str(generator.genKlub())+"');"])
    P.writelines(["\n"])


P.close()

#F. INSERT INTO `almma`.`player` (`id_p`,`name_p`, `last_name_p`, `id_weight`, `id_club`, `id_cat`, `id_weight`, `id_weight`) VALUES ('deafult', 'Junior', 'J');

