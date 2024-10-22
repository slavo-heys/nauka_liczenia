# -*- coding: utf-8 -*-
import os
import random
from datetime import datetime
from datetime import datetime, timedelta
import time
from os import system, name

# os.system('color')


class Program:
    def __init__(self):
        self.i = 0
        self.list_temp = []
        self.CBOLD = '\33[1m'
        self.CITALIC = '\33[3m'
        self.CURL = '\33[4m'
        self.CBLINK = '\33[5m'
        self.CBLINK2 = '\33[6m'
        self.CSELECTED = '\33[7m'

        self.CBLACK = '\33[30m'
        self.CRED = '\33[31m'
        self.CGREEN = '\33[32m'
        self.CYELLOW = '\33[33m'
        self.CBLUE = '\33[34m'
        self.CVIOLET = '\33[35m'
        self.CBEIGE = '\33[36m'
        self.CWHITE = '\33[37m'

        self.CBLACKBG = '\33[40m'
        self.CREDBG = '\33[41m'
        self.CGREENBG = '\33[42m'
        self.CYELLOWBG = '\33[43m'
        self.CBLUEBG = '\33[44m'
        self.CVIOLETBG = '\33[45m'
        self.CBEIGEBG = '\33[46m'
        self.CWHITEBG = '\33[47m'

        self.CGREY = '\33[90m'
        self.CRED2 = '\33[91m'
        self.CGREEN2 = '\33[92m'
        self.CYELLOW2 = '\33[93m'
        self.CBLUE2 = '\33[94m'
        self.CVIOLET2 = '\33[95m'
        self.CBEIGE2 = '\33[96m'
        self.CWHITE2 = '\33[97m'

        self.CGREYBG = '\33[100m'
        self.CREDBG2 = '\33[101m'
        self.CGREENBG2 = '\33[102m'
        self.CYELLOWBG2 = '\33[103m'
        self.CBLUEBG2 = '\33[104m'
        self.CVIOLETBG2 = '\33[105m'
        self.CBEIGEBG2 = '\33[106m'
        self.CWHITEBG2 = '\33[107m'
        self.CEND = '\033[0m'
        self.menu()
        
    def menu(self):
        # czyszczenie ekranu
        self.clear()
        self.imie = input(self.CYELLOW +"\n\tJak masz na imię ? "+self.CEND)

        # czyszczenie ekranu
        self.clear()

        print(self.CYELLOW + "\n\tWitaj " + self.imie + " w programie \"Nauka Liczenia\" w wersji 1.1"+self.CEND)
        print(self.CYELLOW+"\t-----------------------------------------------"+self.CEND)        
        print("\n\n\tWybierz jedną z opcji:\n")
        print("\t 1. dodawanie       4. mnozenie")
        print("\t 2. odejmowanie     5. dzielenie")
        print("\t 3. AUTO            "+self.CRED +
              "0. wyjscie z programu\n"+self.CEND)

        self.wybor = input("\t? ")
        if self.wybor == "1":
            self.dodawanie()
        elif self.wybor == "2":
            self.odejmowanie()
        elif self.wybor == "3":
            self.auto()
        elif self.wybor == "4":
            self.mnozenie()
        elif self.wybor == "5":
            self.dzielenie()
        elif self.wybor == "0":
            exit(0)
        else:
            exit(0)

    def dodawanie(self):
        # czyszczenie ekranu
        self.clear()

        # menu
        self.punkt = 0
        print(self.CYELLOW+"\n\tJesteś w dziale \"Dodawanie\":"+self.CEND)
        print(self.CYELLOW+"\t----------------------------\n"+self.CEND)
        self.ileDzialan = input("\tIle działań chcesz rozwiązać ? ")
        self.podstawa = input("\tPodaj najwyższą liczbę podstawy dodawania ? ")
                
        # losowanie liczb na podstawie zebranych danych
        for self.i in range(1, int(self.ileDzialan)+1):
            # czyszczenie ekranu
            self.clear()

            # losowanie
            self.l1 = random.randint(1, int(self.podstawa))
            self.l2 = random.randint(1, int(self.podstawa))

            # wyswietlenie dzialania do rozwiazania
            self.wynik = self.l1 + self.l2

            #sprawdzanie czy dzialanie istnieje w liscie
            self.dzialanie = str(self.l1)+"+"+str(self.l2)
            spr = self.list_temp.count(self.dzialanie)
            if spr == 0:
                print("\n\t\tDziałanie numer: {}".format(self.i))
                self.odpowiedz = input("\n\t{} + {} = ".format(self.l1, self.l2))
                # dodanie rekordu do listy
                self.list_temp.append(self.dzialanie)
                # sprawdzanie wynikow
                if int(self.odpowiedz) == int(self.wynik):
                    self.punkt += 1
                    print(
                        self.CGREEN+"\t\n BRAWO!!! Wynik prawidłowy, zdobywasz 1 punkt.\n\n"+self.CEND)
                    os.system("pause")
                else:
                    print(
                        self.CRED+"\t\n ZLE!!! Wynik jest nieprawidlowy, powinno byc: {} \n\n".format(self.wynik)+self.CEND)
                    os.system("pause")
            else:
                continue
        
        os.system("pause")
        # czyszczenie ekranu
        self.clear()

        # wyswietlenie wynikow na ekranie
        print(self.CBOLD + self.CVIOLET+"\t\nKoniec, Twoje wyniki:"+self.CEND)
        print("\t - ilość rozwiązanych zadań: "+self.CYELLOW +
              "{}".format(self.ileDzialan)+self.CEND)
        print("\t - poprawnych odpowiedzi: " +
              self.CGREEN+"{}".format(self.punkt)+self.CEND)
        print("\t - blędnych odpowiedzi: "+self.CRED +
              "{}\n\n".format(int(self.ileDzialan) - int(self.punkt))+self.CEND)

        # zapis do pliku txt
        fraza = "{:13s} - ilosc zadan: {} | poprawnych odpowiedzi: {} | bledow: {} | Osoba: {}".format("DODAWANIE",
            self.ileDzialan, self.punkt, int(self.ileDzialan) - int(self.punkt), self.imie)
        self.zapisz(fraza)
        os.system("pause")

        # czyszczenie ekranu
        self.clear()

        # dodatkowe menu
        self.wybor = input(self.CBOLD + self.CVIOLET+"\n Co dalej:"+self.CEND +
                           "\n\t1. powtórz dodawanie\n\t2. powróć do menu głównego\n\t0. wyjscie z programu\n\n? ")
        if self.wybor == "1":
            self.list_temp.clear()
            self.dodawanie()
        elif self.wybor == "2":
            self.list_temp.clear()
            self.menu()
        else:
            exit(0)

    def odejmowanie(self):
        # czyszczenie ekranu
        self.clear()

        # menu
        self.punkt = 0
        print(self.CYELLOW+"\n\tJesteś w dziale \"Odejmowanie\":"+self.CEND)
        print(self.CYELLOW+"\t------------------------------\n"+self.CEND)
        self.ileDzialan = input("\tIle działań chcesz rozwiązać ? ")
        self.podstawa = input(
            "\tPodaj najwyższą liczbę podstawy odejmowania ? ")

        # losowanie liczb na podstawie zebranych danych
        for self.i in range(1, int(self.ileDzialan)+1):
            # czyszczenie ekranu
            self.clear()

            # losowanie
            self.l1 = random.randint(1, int(self.podstawa))
            self.l2 = random.randint(1, int(self.podstawa))

            # wyswietlenie dzialania do rozwiazania
            if self.l1 > self.l2:
                self.wynik = self.l1 - self.l2
                #sprawdzanie czy dzialanie istnieje w liscie
                self.dzialanie = str(self.l1)+"-"+str(self.l2)
                spr = self.list_temp.count(self.dzialanie)
                if spr == 0:
                    print("\n\t\tDziałanie numer: {}".format(self.i))
                    self.odpowiedz = input(
                        "\n\t{} - {} = ".format(self.l1, self.l2))
                    self.list_temp.append(self.dzialanie)
                else:
                    continue
            else:
                self.wynik = self.l2 - self.l1
                #sprawdzanie czy dzialanie istnieje w liscie
                self.dzialanie = str(self.l2)+"-"+str(self.l1)
                spr = self.list_temp.count(self.dzialanie)
                if spr == 0:
                    print("\n\t\tDziałanie numer: {}".format(self.i))
                    self.odpowiedz = input(
                        "\n\t{} - {} = ".format(self.l2, self.l1))
                    self.list_temp.append(self.dzialanie)
                else:
                    continue

            # sprawdzanie wynikow
            if int(self.odpowiedz) == int(self.wynik):
                self.punkt += 1
                print(
                    self.CGREEN+"\t\n BRAWO!!! Wynik prawidłowy, zdobywasz 1 punkt.\n\n"+self.CEND)
                os.system("pause")
            else:
                print(
                    self.CRED+"\t\n ZLE!!! Wynik jest nieprawidlowy, powinno byc: {} \n\n".format(self.wynik)+self.CEND)
                os.system("pause")

        # czyszczenie listy
        self.list_temp.clear()
        
        # czyszczenie ekranu
        self.clear()

        # wyświetlenie wyników
        print("\t\nKoniec, Twoje wyniki:")
        print("\t - ilość rozwiązanych zadań: "+self.CYELLOW +
              "{}".format(self.ileDzialan)+self.CEND)
        print("\t - poprawnych odpowiedzi: " +
              self.CGREEN+"{}".format(self.punkt)+self.CEND)
        print("\t - blędnych odpowiedzi: "+self.CRED +
              "{}\n\n".format(int(self.ileDzialan) - int(self.punkt))+self.CEND)

        # zapis do pliku txt
        fraza = "{:13s} - ilosc zadan: {} | poprawnych odpowiedzi: {} | bledow: {} | Osoba: {}".format("ODEJMOWANIE",
            self.ileDzialan, self.punkt, int(self.ileDzialan) - int(self.punkt), self.imie)
        self.zapisz(fraza)
        os.system("pause")

        # czyszczenie ekranu
        self.clear()

        # dodatkowe menu
        self.wybor = input(self.CBOLD + self.CVIOLET+"\n Co dalej:"+self.CEND +
                           "\n\t1. powtórz odejmowanie\n\t2. powróć do menu głównego\n\t0. wyjscie z programu\n\n? ")
        if self.wybor == "1":
            self.odejmowanie()
        elif self.wybor == "2":
            self.menu()
        else:
            exit(0)

    def mnozenie(self):
        # czyszczenie ekranu
        self.clear()

        # menu
        self.punkt = 0
        print(self.CYELLOW+"\n\tJesteś w dziale \"Mnożenie\":"+self.CEND)
        print(self.CYELLOW+"\t------------------------------\n"+self.CEND)
        self.ileDzialan = input("\tIle działań chcesz rozwiązać ? ")
        self.podstawa = input(
            "\tPodaj najwyższą liczbę podstawy iloczynu (max = 10)? ")
        if int(self.podstawa) > 10:
            self.podstawa = 10

        # losowanie liczb na podstawie zebranych danych
        for self.i in range(1, int(self.ileDzialan)+1):
            # czyszczenie ekranu
            self.clear()

            # losowanie
            self.l1 = random.randint(1, int(self.podstawa))
            self.l2 = random.randint(1, int(self.podstawa))

            # wyswietlenie dzialania do rozwiazania
            self.wynik = self.l1 * self.l2

            #sprawdzanie czy dzialanie istnieje w liscie
            self.dzialanie = str(self.l1)+"*"+str(self.l2)
            spr = self.list_temp.count(self.dzialanie)
            if spr == 0:
                print("\n\t\tDziałanie numer: {}".format(self.i))
                self.odpowiedz = input("\n\t{} * {} = ".format(self.l1, self.l2))

                # sprawdzanie wynikow
                if int(self.odpowiedz) == int(self.wynik):
                    self.punkt += 1
                    print(
                        self.CGREEN+"\t\n BRAWO!!! Wynik prawidłowy, zdobywasz 1 punkt.\n\n"+self.CEND)
                    os.system("pause")
                else:
                    print(
                        self.CRED+"\t\n ZLE!!! Wynik jest nieprawidlowy, powinno byc: {} \n\n".format(self.wynik)+self.CEND)
                    os.system("pause")
            else: continue

        # czyszczenie listy
        self.list_temp.clear()
        # czyszczenie ekranu
        self.clear()

        # wyswietlenie wynikow na ekranie
        print("\t\nKoniec, Twoje wyniki:")
        print("\t - ilość rozwiązanych zadań: "+self.CYELLOW +
              "{}".format(self.ileDzialan)+self.CEND)
        print("\t - poprawnych odpowiedzi: " +
              self.CGREEN+"{}".format(self.punkt)+self.CEND)
        print("\t - blędnych odpowiedzi: "+self.CRED +
              "{}\n\n".format(int(self.ileDzialan) - int(self.punkt))+self.CEND)

        # zapis do pliku txt
        fraza = "{:13s} - ilosc zadan: {} | poprawnych odpowiedzi: {} | bledow: {} | Osoba: {}".format("MNOZENIE",
            self.ileDzialan, self.punkt, int(self.ileDzialan) - int(self.punkt), self.imie)
        self.zapisz(fraza)
        os.system("pause")

        # czyszczenie ekranu
        self.clear()

        # dodatkowe menu
        self.wybor = input(self.CBOLD + self.CVIOLET+"\n  Co dalej:"+self.CEND +
                           "\n\t1. powtórz mnożenie\n\t2. powróć do menu głównego\n\t0. wyjscie z programu\n\n? ")
        if self.wybor == "1":
            self.mnozenie()
        elif self.wybor == "2":
            self.menu()
        else:
            exit(0)

    def dzielenie(self):
        # czyszczenie ekranu
        self.clear()

        # menu
        self.punkt = 0
        print(self.CYELLOW+"\n\tJesteś w dziale \"Dzielenie\":"+self.CEND)
        print(self.CYELLOW+"\t------------------------------\n"+self.CEND)
        self.ileDzialan = input("\tIle działań chcesz rozwiązać ? ")
        self.podstawa = input(
            "\tPodaj najwyższą liczbę podstawy ilorazu (max = 10)? ")
        if int(self.podstawa) > 10:
            self.podstawa = 10

        # losowanie liczb na podstawie zebranych danych
        for self.i in range(1, int(self.ileDzialan)+1):
            # czyszczenie ekranu
            self.clear()

            # losowanie i 3 zmienna
            self.l1 = random.randint(1, int(self.podstawa))
            self.l2 = random.randint(1, int(self.podstawa))
            self.l3 = self.l1 * self.l2

            # wyswietlenie dzialania do rozwiazania
            self.wynik = self.l3 / self.l2

            #sprawdzanie czy dzialanie istnieje w liscie
            self.dzialanie = str(self.l3)+""+str(self.l2)
            spr = self.list_temp.count(self.dzialanie)
            if spr == 0:
                print("\n\t\tDziałanie numer: {}".format(self.i))
                self.odpowiedz = input("\n\t{} : {} = ".format(self.l3, self.l2))

                # sprawdzanie wynikow
                if int(self.odpowiedz) == int(self.wynik):
                    self.punkt += 1
                    print(
                        self.CGREEN+"\t\n BRAWO!!! Wynik prawidłowy, zdobywasz 1 punkt.\n\n"+self.CEND)
                    os.system("pause")
                else:
                    print(self.CRED+"\t\n ZLE!!! Wynik jest nieprawidlowy, powinno byc: {} \n\n".format(
                        int(self.wynik))+self.CEND)
                    os.system("pause")
            else:
                continue
        
        # czyszczenie listy
        self.list_temp.clear()

        # czyszczenie ekranu
        self.clear()

        # wyswietlenie wynikow na ekranie
        print("\t\nKoniec, Twoje wyniki:")
        print("\t - ilość rozwiązanych zadań: "+self.CYELLOW +
              "{}".format(self.ileDzialan)+self.CEND)
        print("\t - poprawnych odpowiedzi: " +
              self.CGREEN+"{}".format(self.punkt)+self.CEND)
        print("\t - blędnych odpowiedzi: "+self.CRED +
              "{}\n\n".format(int(self.ileDzialan) - int(self.punkt))+self.CEND)

        # zapis do pliku txt
        fraza = "{:13s} - ilosc zadan: {} | poprawnych odpowiedzi: {} | bledow: {} | Osoba: {}".format("DZIELENIE",
            self.ileDzialan, self.punkt, int(self.ileDzialan) - int(self.punkt), self.imie)
        self.zapisz(fraza)
        os.system("pause")

        # czyszczenie ekranu
        self.clear()

        # dodatkowe menu
        self.wybor = input(self.CBOLD + self.CVIOLET+"\nCo dalej:"+self.CEND +
                           "\n\t1. powtórz dzielenie\n\t2. powróć do menu głównego\n\t0. wyjscie z programu\n\n? ")
        if self.wybor == "1":
            self.dzielenie()
        elif self.wybor == "2":
            self.menu()
        else:
            exit(0)

    def auto(self):
        # czyszczenie ekranu
        self.clear()

        # menu
        self.punkt = 0
        print(self.CYELLOW+"\t\n Jesteś w dziale \"AUTO\", uważnie sprawdzaj znak działania"+self.CEND)
        print(self.CYELLOW+"\t\n --------------------------------------------------------\n\n"+self.CEND)
        self.ileDzialan = input("\tIle działań chcesz rozwiązać ? ")
        self.podstawa = input("\tPodaj najwyższą liczbę podstawy działań ? ")
        czas_start = datetime.now()

        for self.i in range(1, int(self.ileDzialan)+1):
            # czyszczenie ekranu
            self.clear()

            print("\t\n Działanie numer: {}".format(self.i))

            # losowanie dzialania: 1 - dodawanie, 2. odejmowanie, 3. mnozenie, 4. dzielenie
            i_los = random.randint(1, 5)
            if i_los == 1:
                # losowanie / dodawanie
                self.l1 = random.randint(1, int(self.podstawa))
                self.l2 = random.randint(1, int(self.podstawa))
                self.wynik = self.l1 + self.l2
                self.odpowiedz = input(
                    "\n\t{} + {} = ".format(self.l1, self.l2))

                # sprawdzanie wynikow
                if int(self.odpowiedz) == self.wynik:
                    self.punkt += 1
                    print(
                        self.CGREEN+"\t\n BRAWO!!! Wynik prawidłowy, zdobywasz 1 punkt.\n\n"+self.CEND)
                    os.system("pause")
                else:
                    print(self.CRED+"\t\n ZLE!!! Wynik jest nieprawidlowy, powinno byc: {} \n\n".format(
                        int(self.wynik))+self.CEND)
                    fraza_dzialania = "    {:2s} + {:2s} = {:3s} |    powinno byc {:3s}".format(
                        str(self.l1), str(self.l2), str(self.odpowiedz), str(self.wynik))
                    self.zapisz_dzialania(fraza_dzialania)
                    os.system("pause")
            elif i_los == 2:
                # losowanie / odejmowanie
                self.l1 = random.randint(1, int(self.podstawa))
                self.l2 = random.randint(1, int(self.podstawa))
                if self.l1 > self.l2:
                    self.wynik = self.l1 - self.l2
                    self.odpowiedz = input(
                        "\n\t{} - {} = ".format(self.l1, self.l2))
                else:
                    self.wynik = self.l2 - self.l1
                    self.odpowiedz = input(
                        "\n\t{} - {} = ".format(self.l2, self.l1))

                 # sprawdzanie wynikow
                if int(self.odpowiedz) == int(self.wynik):
                    self.punkt += 1
                    print(
                        self.CGREEN+"\t\n BRAWO!!! Wynik prawidłowy, zdobywasz 1 punkt.\n\n"+self.CEND)
                    os.system("pause")
                else:
                    print(self.CRED+"\t\n ZLE!!! Wynik jest nieprawidlowy, powinno byc: {} \n\n".format(
                        int(self.wynik))+self.CEND)
                    fraza_dzialania = "    {:2s} - {:2s} = {:3s} |    powinno byc {:3s}".format(
                        str(self.l1), str(self.l2), str(self.odpowiedz), str(self.wynik))
                    self.zapisz_dzialania(fraza_dzialania)
                    os.system("pause")
            elif i_los == 3:
                # losowanie / mnozenie
                self.l1 = random.randint(1, 10)
                self.l2 = random.randint(1, 10)
                self.wynik = self.l1 * self.l2
                self.odpowiedz = input(
                    "\n\t{} * {} = ".format(self.l1, self.l2))

                # sprawdzanie wynikow
                if int(self.odpowiedz) == int(self.wynik):
                    self.punkt += 1
                    print(
                        self.CGREEN+"\t\n BRAWO!!! Wynik prawidłowy, zdobywasz 1 punkt.\n\n"+self.CEND)
                    os.system("pause")
                else:
                    print(self.CRED+"\t\n ZLE!!! Wynik jest nieprawidlowy, powinno byc: {} \n\n".format(
                        int(self.wynik))+self.CEND)
                    fraza_dzialania = "    {:2s} * {:2s} = {:3s} |    powinno byc {:3s}".format(
                        str(self.l1), str(self.l2), str(self.odpowiedz), str(self.wynik))
                    self.zapisz_dzialania(fraza_dzialania)
                    os.system("pause")
            else:
                # losowanie / dzielenie
                self.l1 = random.randint(1, 10)
                self.l2 = random.randint(1, 10)
                self.l3 = self.l1 * self.l2
                # wyswietlenie dzialania do rozwiazania
                self.wynik = self.l3 / self.l2
                self.odpowiedz = input(
                    "\n\t{} : {} = ".format(self.l3, self.l2))

                # sprawdzanie wynikow
                if int(self.odpowiedz) == self.wynik:
                    self.punkt += 1
                    print(
                        self.CGREEN+"\t\n BRAWO!!! Wynik prawidłowy, zdobywasz 1 punkt.\n\n"+self.CEND)
                    os.system("pause")
                else:
                    print(self.CRED+"\t\n ZLE!!! Wynik jest nieprawidlowy, powinno byc: {} \n\n".format(
                        int(self.wynik))+self.CEND)
                    fraza_dzialania = "    {:2s} : {:2s} = {:3s} |    powinno byc {:3s}".format(
                        str(self.l3), str(self.l2), str(self.odpowiedz), str(self.wynik))
                    self.zapisz_dzialania(fraza_dzialania)
                    os.system("pause")

        # obliczanie czasu
        czas_koniec = datetime.now()
        czas_zostalo = (czas_koniec - czas_start).seconds
        czas_zostalo_1 = str(czas_zostalo) + " sek."
        if int(czas_zostalo) > 60:
            czas_zostalo = czas_zostalo/60
            czas_zostalo = round(czas_zostalo, 2)
            czas_zostalo_1 = str(czas_zostalo) + " min."

        # czyszczenie ekranu
        self.clear()

        # wyświetlenie wyników
        print(self.CBOLD + self.CVIOLET+"\t\nKoniec, Twoje wyniki:"+self.CEND)
        print("\t - czas rozpoczęcia: {}\n\t - czas zakończenia: {}\n\t - rozwiązanie zadań zajęło Ci: {}".format(
            czas_start, czas_koniec, czas_zostalo_1))
        print("\t - ilość rozwiązanych zadań: "+self.CYELLOW +
              "{}".format(self.ileDzialan)+self.CEND)
        print("\t - poprawnych odpowiedzi: " +
              self.CGREEN+"{}".format(self.punkt)+self.CEND)
        print("\t - blędnych odpowiedzi: "+self.CRED +
              "{}\n\n".format(int(self.ileDzialan) - int(self.punkt))+self.CEND)

        # zapis do pliku txt
        fraza = "AUTO - ilosc zadan: {:3s} | poprawnych odpowiedzi: {:3s} | bledow: {:3s} | czas: {:5s} | Osoba: {}".format(
            str(self.ileDzialan), str(self.punkt), str(int(self.ileDzialan) - int(self.punkt)), czas_zostalo_1, self.imie)
        self.zapisz(fraza)
        os.system("pause")

        # czyszczenie ekranu
        self.clear()

        # dodatkowe menu
        self.wybor = input(self.CBOLD + self.CVIOLET+"\nCo dalej:"+self.CEND +
                           "\n\t1. powtórz liczenie\n\t2. powróć do menu głównego\n\t0. wyjscie z programu\n\n? ")
        if self.wybor == "1":
            self.auto()
        elif self.wybor == "2":
            self.menu()
        else:
            exit(0)

    def zapisz(self, wynik):
        now = datetime.now()
        data = now.strftime("%Y-%b-%d")
        fraza = data + " " + wynik
        plik = open('wynik_dzialan_matematycznych.txt', 'a')
        plik.writelines(str(fraza)+"\n")
        plik.close()

    def zapisz_dzialania(self, dzialanie):
        now = datetime.now()
        data = now.strftime("%Y-%b-%d")
        fraza = self.imie + "   " + data + "   " + dzialanie
        tytul = (now.strftime("%Y-%b-%d")+".txt")
        plik = open(tytul, 'a')
        plik.writelines(str(fraza)+"\n")
        plik.close()

    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')


start = Program()


