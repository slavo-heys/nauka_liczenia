import tkinter as tk

def new_file_clicked(event=None):
    print("The New File menu was clicked!")

root = tk.Tk()
root.title("Menubar in Tk")
root.geometry("400x300")
menubar = tk.Menu()
file_menu = tk.Menu(menubar, tearoff=False)
new_file_img = tk.PhotoImage(file="new_file.png")
file_menu.add_command(
    label="New",
    accelerator="Ctrl+N",
    command=new_file_clicked,
    image=new_file_img,
    # The image must be placed to the left of the text.
    compound=tk.LEFT
)
root.bind_all("<Control-n>", new_file_clicked)
root.bind_all("<Control-N>", new_file_clicked)
menubar.add_cascade(menu=file_menu, label="File")
root.config(menu=menubar)
root.mainloop()