from tkinter import *
import mysql.connector
import sys
import config
from tkinter import ttk

usr = config.mysql['user']
pwd = config.mysql['password']
hst = config.mysql['host']
dab = 'cpsc321'
# create a connection
#con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)
#con.close()
root = Tk()
root.title("Recipes")
root.geometry("500x500")

my_notebook = ttk.Notebook(root)
my_notebook.pack()

my_frame1 = Frame(my_notebook, width= 500, height = 500, bg = "blue")
my_frame2 = Frame(my_notebook, width= 500, height = 500, bg = "red")

my_frame1.pack(fill = "both", expand = 1)
my_frame2.pack(fill = "both", expand = 1)

my_notebook.add(my_frame1, text = "Recipe Search")
my_notebook.add(my_frame2, text = "Meal Search")


#tab1 = ttk.Frame(MenuBar)
#MenuBar.add(tab1, text='Recipe Search')
#tab2 = ttk.Frame(MenuBar)
#MenuBar.add(tab1, text='Meal Search')

root.mainloop()
