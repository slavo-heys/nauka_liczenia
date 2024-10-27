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
        plik_img = PhotoImage(file="file.png")
        open_img = PhotoImage(file="open.png")
        save_img = PhotoImage(file="save.png")
        close_img = PhotoImage(file="close.png")
        suma_img = PhotoImage(file="sum.png")
        minus_img = PhotoImage(file="minus.png")
        mnozenie_img = PhotoImage(file="mnozenie.png")
        dzielenie_img = PhotoImage(file="dzielenie.png")
        auto_img = PhotoImage(file="automat.png")

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

    def kliknij_wczytaj(self, event=None):
        print("Kliknąłeś otwórz")

    def kliknij_zapisz(self, event=None):
        print("Kliknąłeś zapisz")

    def dodawanie(self, event=None):
        print("dodawanie")

    def odejmowanie(self, event=None):
        print("odejmowanie")

    def mnozenie(self, event=None):
        print("mnozenie")

    def dzielenie(self, event=None):
        print("dzielenie")

    def automat(self, event=None):
        print("automat")

start = Program()
