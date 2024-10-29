'''
Program "nauka liczenia" w wersji okienkowej.
Program w fazie tworzenia

autor: Slavo Heys
data rozpoczęcia: 27.10.2024
'''

from tkinter import *
from tkinter import messagebox
import random
from datetime import datetime
import time

class Program:
    def __init__(self) -> None:        
        self.root = Tk()
        self.root.title("Nauka liczenia v 2.0")
        self.root.geometry("800x600")

        # deklaracja zmiennych
        self.imie_inp = StringVar()
        self.wiek_inp = StringVar()
        self.podstawa_inp = StringVar()
        self.ilosc_inp = StringVar()
        self.wynik = StringVar()
        self.i = 0
        self.poprawne = 0
        self.bledna = 0
                
        # menu na listwie górnej
        menu = Menu(self.root)
        self.root.config(menu=menu)

        # skrót klawiszowy wczytaj
        self.root.bind_all("<Control-n>", self.kliknij_wczytaj)
        self.root.bind_all("<Control-N>", self.kliknij_wczytaj)

        # skrót klawiszowy zapisz
        self.root.bind_all("<Control-z>", self.kliknij_zapisz)
        self.root.bind_all("<Control-Z>", self.kliknij_zapisz)

        # skrót klawiszowy zamknij
        self.root.bind_all("<Control-e>", self.zamknij_program)
        self.root.bind_all("<Control-E>", self.zamknij_program)

        # skrót klawiszowy dodawanie
        self.root.bind_all("<Control-s>", self.dodawanie_menu)
        self.root.bind_all("<Control-S>", self.dodawanie_menu)

        # skrót klawiszowy odejmowanie
        self.root.bind_all("<Control-r>", self.odejmowanie)
        self.root.bind_all("<Control-R>", self.odejmowanie)

        # skrót klawiszowy mnozenie
        self.root.bind_all("<Control-m>", self.mnozenie)
        self.root.bind_all("<Control-M>", self.mnozenie)

        # skrót klawiszowy dzielenie
        self.root.bind_all("<Control-d>", self.dzielenie)
        self.root.bind_all("<Control-D>", self.dzielenie)

        # skrót klawiszowy automat
        self.root.bind_all("<Control-a>", self.automat)
        self.root.bind_all("<Control-A>", self.automat)

        # deklaracja ikon w przyciskach
        plik_img = PhotoImage(file="./img/file.png")
        open_img = PhotoImage(file="./img/open.png")
        save_img = PhotoImage(file="./img/save.png")
        close_img = PhotoImage(file="./img/close.png")
        suma_img = PhotoImage(file="./img/sum.png")
        minus_img = PhotoImage(file="./img/minus.png")
        mnozenie_img = PhotoImage(file="./img/mnozenie.png")
        dzielenie_img = PhotoImage(file="./img/dzielenie.png")
        auto_img = PhotoImage(file="./img/automat.png")

        filemenu = Menu(menu, tearoff=False)
        menu.add_cascade(label='Plik', menu=filemenu)

        # deklaracja podmenu Plik na listwie
        filemenu.add_command(label='Wczytaj', accelerator="Ctrl+N", command=self.kliknij_wczytaj, image=open_img, compound=LEFT)
        filemenu.add_command(label='Zapisz', accelerator="Ctrl+Z", command=self.kliknij_zapisz, image=save_img, compound=LEFT)
        filemenu.add_separator()
        filemenu.add_command(label='Zamknij', accelerator="Ctrl+E", command=self.root.quit, image=close_img, compound=LEFT)
        # deklaracja podmenu Dzialania na listwie
        dzialaniamenu = Menu(menu, tearoff=False)
        menu.add_cascade(label='Działania', menu=dzialaniamenu,)
        dzialaniamenu.add_command(label='Dodawanie', accelerator="Ctrl+D", command=self.dodawanie_menu, image=suma_img, compound=LEFT)
        dzialaniamenu.add_command(label='Odejmowanie', accelerator="Ctrl+R", command=self.odejmowanie, image=minus_img, compound=LEFT)
        dzialaniamenu.add_command(label='Mnożenie', accelerator="Ctrl+M", command=self.mnozenie, image=mnozenie_img, compound=LEFT)
        dzialaniamenu.add_command(label='Dzielenie', accelerator="Ctrl+D", command=self.dzielenie, image=dzielenie_img, compound=LEFT)
        dzialaniamenu.add_separator()
        dzialaniamenu.add_command(label='Automat', accelerator="Ctrl+A", command=self.automat, image=auto_img, compound=LEFT)
        # deklaracja podmenu Pomoc na listwie
        helpmenu = Menu(menu, tearoff=False)
        menu.add_cascade(label='Pomoc', menu=helpmenu)
        helpmenu.add_command(label='About')

        self.root.mainloop()

    def zamknij_program(self, event=None):
        command=self.root.quit
    
    def wyczysc_pola(self, event=None):
        self.input_imie.delete(0, END)
        self.input_wiek.delete(0, END)
        self.input_podstawa_dodawania.delete(0, END)
        self.input_ilosc_dzialan.delete(0, END)

    def poprawny_wynik(self,wynik_user):
        wynik_p = self.wynik.get()
        wynik_p = int(wynik_p)
        wynik_user_p = wynik_user
        wynik_user_p = int(wynik_user_p)

        

        if wynik_user_p == wynik_p:
            self.ramka3 = LabelFrame(self.root, text="Sprawdzanie poprawności:", fg = "green", padx = 2, pady = 5)
            self.ramka3.pack(padx=0, pady=5) 
            print("wynik poprawny")
            text6 = Label(self.ramka3, text="Wynik poprawny!!!", font=("Arial", 12), fg= "green")
            text6.pack(padx=0, pady=5)
            time.sleep(3)
        else:
            self.ramka3 = LabelFrame(self.root, text="Sprawdzanie poprawności:", fg = "green", padx = 2, pady = 5)
            self.ramka3.pack(padx=0, pady=5) 
            print("wynik niepoprawny")
            text6 = Label(self.ramka3, text="Wynik niepoprawny!!!", font=("Arial", 12), fg= "red")
            text6.pack(padx=0, pady=5)
            time.sleep(3)        
        
        self.ramka3.destroy()
        

    def dzialanie_dodawanie(self):
        self.imie = self.imie_inp.get()
        self.wiek = self.wiek_inp.get()
        self.podstawa = self.podstawa_inp.get()
        self.ilosc = self.ilosc_inp.get()
        if self.imie=="" or self.wiek=="":
            messagebox.showerror("Błąd", "Brakuje wartości w polu IMIE lub WIEK!!!")               
            self.ramka.destroy()
            self.ramka1.destroy()
            
            self.dodawanie_menu()
        else:
            try:  
                self.wiek = int(self.wiek)            
            except:
                messagebox.showerror("Błąd", "Wiek nie jest cyfrą!!!")                           
                self.ramka.destroy()
                self.ramka1.destroy()
                self.dodawanie_menu()   

        try:
            self.podstawa = int(self.podstawa)
            self.ilosc = int(self.ilosc)
        except:
            self.podstawa = 50
            self.ilosc = 100   

        self.ramka1.destroy()

        self.ramka2 = LabelFrame(self.root, text="Działanie: ", fg = "green", padx = 2, pady = 5)
        self.ramka2.pack(padx=0, pady=20) 

        text1 = Label(self.ramka2, text = "Ile jest:", font=("Arial", 12, "bold"), foreground="silver")
        text1.grid(row=0, column=1)

        for self.i in range(self.ilosc):
            a = random.randint(1, int(self.podstawa))
            b = random.randint(1, int(self.podstawa))           

            suma_wynik = a + b
            
            text2 = Label(self.ramka2)
            text2.grid(row=1, column=0)

            text3 = Label(self.ramka2, text = str(a)+" + "+str(b)+" = ", font=("Arial", 20), foreground="green")
            text3.grid(row=2, column=1)
            
            text4 = Entry(self.ramka2, textvariable=self.wynik, width = 5, font=("Arial", 20), fg= "white", bg = "green")
            text4.grid(row=2, column=2)

            text5 = Label(self.ramka2)
            text5.grid(row=3, column=0)

            button = Button(self.ramka2, text="Sprawdź wynik", fg="white", bg="red", command=lambda: self.poprawny_wynik(suma_wynik))
            button.grid(row=4,column=1)

            button1 = Button(self.ramka2, text="Popraw wynik", fg="white", bg="black", command=text4.delete(0,END))
            button1.grid(row=4,column=2)

            
    def kliknij_wczytaj(self, event=None):
        print("Kliknąłeś otwórz")

    def kliknij_zapisz(self, event=None):
        print("Kliknąłeś zapisz")

    def dodawanie_menu(self, event=None):
        self.ramka = LabelFrame(self.root, padx = 2, pady = 2)
        self.ramka.pack(padx=0, pady=2)
                       
        wstep_text = Label(self.ramka, text="Jesteś w dziale \"Dodawanie\"", font =("Courier", 16, "bold"), foreground="blue", justify="center")
        wstep_text.pack(pady=5, padx=180)        

        self.ramka1 = LabelFrame(self.root, text="Podaj informacje", fg = "green", padx = 2, pady = 5)
        self.ramka1.pack(padx=0, pady=20) 

        self.imie_text = Label(self.ramka1, text= "Twoje imie: ", font =("Courier", 11), justify=LEFT)
        self.imie_text.grid(row=0, column=0)
        self.input_imie = Entry(self.ramka1, textvariable=self.imie_inp, width = 25, bg = "light yellow")
        self.input_imie.grid(row=0, column=1)

        self.wiek_text = Label(self.ramka1, text= "Ile masz lat: ", justify=LEFT, font =("Courier", 11))
        self.wiek_text.grid(row=1, column=0)
        self.input_wiek = Entry(self.ramka1, textvariable=self.wiek_inp, width = 25, bg = "light yellow")
        self.input_wiek.grid(row=1, column=1)

        self.podstawa_dodawania_text = Label(self.ramka1, text= "Najwyższa podstawa działania: ", font =("Courier", 11))
        self.podstawa_dodawania_text.grid(row=2, column=0)
        self.input_podstawa_dodawania = Entry(self.ramka1, textvariable=self.podstawa_inp, width = 25, bg = "light yellow")
        self.input_podstawa_dodawania.grid(row=2, column=1)

        self.ilosc_dzialan_text = Label(self.ramka1, text = "Ilość działań:", justify=LEFT, font=("Courier", 11))
        self.ilosc_dzialan_text.grid(row=3, column=0)
        self.input_ilosc_dzialan = Entry(self.ramka1,textvariable=self.ilosc_inp, width = 25, bg = "light yellow")
        self.input_ilosc_dzialan.grid(row=3, column=1)

        self.ilosc_dzialan_text = Label(self.ramka1, text = "", justify=LEFT, font=("Courier", 11))
        self.ilosc_dzialan_text.grid(row=4, column=0)

        przycisk_1 = Button(self.ramka1, text="Zapisz, przejdź dalej", font =("Courier", 11, "bold"), foreground="white", background="red", justify="center", command=self.dzialanie_dodawanie).grid(row=5, column=0)
        przycisk_2 = Button(self.ramka1, text="Wyczyść pola", font =("Courier", 11, "bold"), foreground="white", background="black", justify="center", command=self.wyczysc_pola).grid(row=5, column=1)   
             

    def odejmowanie(self, event=None):
        print("odejmowanie")

    def mnozenie(self, event=None):
        print("mnozenie")

    def dzielenie(self, event=None):
        print("dzielenie")

    def automat(self, event=None):
        print("automat")

start = Program()
