from tkinter import *

import mysql.connector
import sys
import config
from tkinter import ttk
import tkinter as tk

usr = config.mysql['user']
pwd = config.mysql['password']
hst = config.mysql['host']
dab = 'asmith37_DB'
# create a connection
con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)
#con.close()
root = Tk()
root.title("Recipes")

#root.geometry("400x400")

#MenuBar = ttk.Notebook(root)
#MenuBar.pack()

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

mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


#login = StringVar()
ttk.Label(mainframe, text="login").grid(column=3, row=1)

username = StringVar()
name = ttk.Entry(mainframe, textvariable=username)
name.grid(column = 3, row=2)

#loginUsername = username.get()
#rs = con.cursor()
#query = '''SELECT COUNT(*)
#            FROM user 
#            WHERE username = %s'''
#rs.execute(query, (loginUsername))


def login():
    loginUsername = username.get()
    print(loginUsername)
    rs = con.cursor()
    query = '''SELECT COUNT(*)
                FROM user 
                WHERE username = %s'''
    rs.execute(query, (loginUsername)) 

ttk.Button(mainframe, text="login", command=login).grid(column=3, row=3, sticky=(W,E))

root.mainloop()
