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
con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

root = Tk()
root.title("Recipes")
root.geometry("400x400")
con.close()
#MenuBar = ttk.Notebook(root)
#MenuBar.pack()
#tab1 = ttk.Frame(MenuBar)
#MenuBar.add(tab1, text='Recipe Search')
#tab2 = ttk.Frame(MenuBar)
#MenuBar.add(tab1, text='Meal Search')

root.mainloop()
