from tkinter import *
#from PIL import ImageTK, ImageTK
from tkinter import ttk
root = Tk()
root.title("Recipes")
root.geometry("400x400")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

login = StringVar()
ttk.Label(mainframe, textvariable="login").grid(column=2, row=2, sticky=(W, E))

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=1, row=1, sticky=(W, E))

root.mainloop()
