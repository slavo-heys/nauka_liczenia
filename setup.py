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
        self.root.title("Paper, Rock, Scissors")
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

        # deklaracja ikon w przyciskach
        plik_img = PhotoImage(file="file.png")
        open_img = PhotoImage(file="open.png")
        save_img = PhotoImage(file="save.png")
        close_img = PhotoImage(file="close.png")

        filemenu = Menu(menu, tearoff=False)
        menu.add_cascade(label='Plik', menu=filemenu)

        # deklaracja podmenu Plik na listwie
        filemenu.add_command(label='Wczytaj', accelerator="Ctrl+N", command=self.kliknij_wczytaj, image=open_img, compound=LEFT)
        filemenu.add_command(label='Zapisz', accelerator="Ctrl+Z", command=self.kliknij_zapisz, image=save_img, compound=LEFT)
        filemenu.add_separator()
        filemenu.add_command(label='Zamknij', accelerator="Ctrl+E", command=self.root.quit, image=close_img, compound=LEFT)
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

start = Program()
