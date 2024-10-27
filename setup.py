from tkinter import *

root = Tk()
root.title("Paper, Rock, Scissors")
root.geometry("800x600")

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=False)
menu.add_cascade(label='Plik', menu=filemenu)
filemenu.add_command(label='Wczytaj')
filemenu.add_command(label='Zapisz')
filemenu.add_separator()
filemenu.add_command(label='Zamknij', command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label='Pomoc', menu=helpmenu)
helpmenu.add_command(label='About')

root.mainloop()
