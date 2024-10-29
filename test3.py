import tkinter as tk

def function(widget):
    print(widget['text'])

root = tk.Tk()

button1 = tk.Button(root, text='Yes')
button1.pack()
button1["command"] = lambda:function(button1)

button2 = tk.Button(root, text='No')
button2.pack()
button2["command"] = lambda:function(button2)

root.mainloop()
