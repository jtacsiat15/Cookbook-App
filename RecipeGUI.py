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

"""ttk.Label(root, text="Login").grid(column=3, row=1)

username = StringVar()
name = ttk.Entry(root, textvariable=username)
name.grid(column = 3, row=2)

password = StringVar()
name = ttk.Entry(root, textvariable=password)
name.grid(column = 3, row=3)"""

"""def login():
    loginUsername = username.get()
    loginPassword = password.get()
    print(loginUsername)
    print(loginPassword)
    rs = con.cursor()
    getPassword = '''SELECT password
                FROM User 
                WHERE username = "%s"'''
    
    rs.execute(getPassword % (loginUsername))
    row = rs.fetchone()
    if row is not None:
        print(row[0])
        if (row[0] == loginPassword):
            print("login successful")
        else:
            print("incorrect password")
    else:
        print("incorrect username")
    #getPassword = '''SELECT Password
    #                    FROM User
    #                    WHERE username = "%s"'''

    #rs.execute(getPassword % (loginUsername))


ttk.Button(root, text="login", command=login).grid(column=3, row=4, sticky=(W,E))"""

#def runApp():
my_notebook = ttk.Notebook(root)
my_notebook.pack()

recipeFrame = Frame(my_notebook, width= 500, height = 500)
mealSearchFrame = Frame(my_notebook, width= 500, height = 500)
profileFrame = Frame(my_notebook, width= 500, height = 500)

recipeFrame.pack(fill = "both", expand = 1)
mealSearchFrame.pack(fill = "both", expand = 1)
profileFrame.pack(fill = "both", expand = 1)

my_notebook.add(recipeFrame, text = "Recipe Search")
my_notebook.add(mealSearchFrame, text = "Meal Search")
my_notebook.add(profileFrame, text = "Profile")


#display the meal list

def go(event): 
    print("here")
    mealName = mealList.get(mealList.curselection())
    print(mealName)

mealList = Listbox(mealSearchFrame, width = 40)
rs = con.cursor()
getMealNames = '''SELECT meal_name
                    FROM Meal'''
rs.execute(getMealNames)
count = 0
for meal in rs:
    count += 1
    mealList.insert(count, str(meal)[2:-3])

mealList.bind('<Double-1>', go)

mealList.pack()

#login = StringVar()
"""ttk.Label(profileFrame, text="Login").grid(column=3, row=1)

username = StringVar()
name = ttk.Entry(profileFrame, textvariable=username)
name.grid(column = 3, row=2)

def login():
    loginUsername = username.get()
    print(loginUsername)
    rs = con.cursor()
    query = '''SELECT COUNT(*)
                FROM User 
                WHERE username = "%s"'''
    rs.execute(query % (loginUsername))

ttk.Button(profileFrame, text="login", command=login).grid(column=3, row=3, sticky=(W,E))"""



root.mainloop()
