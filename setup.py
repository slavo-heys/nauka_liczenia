'''
Program "nauka liczenia" w wersji okienkowej.
Program w fazie tworzenia

autor: Slavo Heys
data rozpoczęcia: 27.10.2024
'''

from tkinter import *

class Program:
    def __init__(self) -> None:        
        self.root = Tk()
        self.root.title("Nauka liczenia v 2.0")
        self.root.geometry("800x600")

        # deklaracja ramek
        self.ramka = LabelFrame(self.root, padx = 2, pady = 2)
        self.ramka.pack(padx=0, pady=2)  

        self.ramka1 = LabelFrame(self.root, padx = 2, pady = 5)
        self.ramka1.pack(padx=0, pady=3)
        
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
        self.root.bind_all("<Control-s>", self.dodawanie)
        self.root.bind_all("<Control-S>", self.dodawanie)

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
        dzialaniamenu.add_command(label='Dodawanie', accelerator="Ctrl+D", command=self.dodawanie, image=suma_img, compound=LEFT)
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

    def info(self):
        
        self.imie_text = Label(self.ramka1, text= "Twoje imie: ", font =("Courier", 11), justify=LEFT).grid(row=0, column=0)
        self.input_imie = Text(self.ramka1, height = 1, width = 25, bg = "light yellow").grid(row=0, column=1)

        self.wiek_text = Label(self.ramka1, text= "Ile masz lat: ", justify=LEFT, font =("Courier", 11)).grid(row=1, column=0)
        self.input_wiek = Text(self.ramka1, height = 1, width = 25, bg = "light yellow").grid(row=1, column=1)

        self.podstawa_dodawania_text = Label(self.ramka1, text= "Najwyższa podstawa działania: ", font =("Courier", 11)).grid(row=2, column=0)
        self.input_podstawa_dodawania = Text(self.ramka1, height = 1, width = 25, bg = "light yellow").grid(row=2, column=1)

        self.ilosc_dzialan_text = Label(self.ramka1, text = "Ilość działań:", justify=LEFT, font=("Courier", 11)).grid(row=3, column=0)
        self.input_ilosc_dzialan = Text(self.ramka1, height = 1, width = 25, bg = "light yellow").grid(row=3, column=1)

        self.ilosc_dzialan_text = Label(self.ramka1, text = "", justify=LEFT, font=("Courier", 11)).grid(row=4, column=0)

        przycisk_1 = Button(self.ramka1, text="Zapisz, przejdź dalej", font =("Courier", 11, "bold"), foreground="white", background="red", justify="center").grid(row=5, column=0)
        przycisk_2 = Button(self.ramka1, text="Wyczyść pola", font =("Courier", 11, "bold"), foreground="white", background="black", justify="center").grid(row=5, column=1)

    def kliknij_wczytaj(self, event=None):
        print("Kliknąłeś otwórz")

    def kliknij_zapisz(self, event=None):
        print("Kliknąłeś zapisz")

    def dodawanie(self, event=None):   
             
        wstep_text = Label(self.ramka, text="Jesteś w dziale \"Dodawanie\"", font =("Courier", 16, "bold"), foreground="blue", justify="center")
        wstep_text.pack(pady=5, padx=180)
        self.info()        

    def odejmowanie(self, event=None):
        print("odejmowanie")

    def mnozenie(self, event=None):
        print("mnozenie")

    def dzielenie(self, event=None):
        print("dzielenie")

    def automat(self, event=None):
        print("automat")

start = Program()
