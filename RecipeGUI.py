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
"""
ttk.Label(root, text="Login").grid(column=3, row=1)

username = StringVar()
name = ttk.Entry(root, textvariable=username)
name.grid(column = 3, row=2)

password = StringVar()
name = ttk.Entry(root, textvariable=password)
name.grid(column = 3, row=3)
"""
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

usernameLabel = ttk.Label(recipeFrame, text="Enter usernames (separated by commas):").grid(column=1, row=1)
usernameField = ttk.Entry(recipeFrame, width = 20)
usernameField.grid(column=2, row = 1)

IngredientLabel = ttk.Label(recipeFrame, text="Enter ingredients (separated by commas):").grid(column=1, row=2)
IngredientField = ttk.Entry(recipeFrame, width = 20)
IngredientField.grid(column=2, row = 2)

toolLabel = ttk.Label(recipeFrame, text="Enter cooking tools (separated by commas):").grid(column=1, row=3)
toolField = ttk.Entry(recipeFrame, width = 20)
toolField.grid(column=2, row = 3)

toolLabel = ttk.Label(recipeFrame, text="Enter cooking tools (separated by commas):").grid(column=1, row=3)
toolField = ttk.Entry(recipeFrame, width = 20)
toolField.grid(column=2, row = 3)

dietLabel = ttk.Label(recipeFrame, text="Enter dietary restrictions (separated by commas):").grid(column=1, row=4)
dietField = ttk.Entry(recipeFrame, width = 20)
dietField.grid(column=2, row = 4)

cuisineLabel = ttk.Label(recipeFrame, text="Enter cuisine type (separated by commas):").grid(column=1, row=5)
cuisineField = ttk.Entry(recipeFrame, width = 20)
cuisineField.grid(column=2, row = 5)

def search():
    query = ""

    usernames = usernameField.get()
    if(usernames != ""):
        users = usernames.split(",")
        usernameInput = str([u.lstrip().rstrip() for u in users])
        usernameInput = usernameInput[1:-1]
        q = '''SELECT r1.recipe_title, r1.recipe_id
                FROM User u1 JOIN Recipe r1 ON (r1.username = u1.username)
                WHERE u1.username IN ({users}) OR u1.name IN ({users})'''.format(users = usernameInput)
        query += q

    ingredients = IngredientField.get()
    if(ingredients != ""):
        ing_lst = ingredients.split(",")
        input = str([i.lstrip().rstrip() for i in ing_lst])
        input = input[1:-1]
        q = '''SELECT DISTINCT r1.recipe_title, r1.recipe_id
                FROM Recipe r1 JOIN IngredientOf i1 ON (r1.recipe_id = i1.recipe_id)
                    JOIN Ingredient i2 ON (i1.ingredient_id = i2.ingredient_id)
                WHERE i2.ingredient_name IN ({ingredients})'''.format(ingredients = input)
        if query == "":
            query += q
        else :
            query += (" INTERSECT " + q)

    tools = toolField.get()
    if(tools != ""):
        tool_lst = tools.split(",")
        input = str([i.lstrip().rstrip() for i in tool_lst])
        input = input[1:-1]
        q = '''SELECT DISTINCT r1.recipe_title, r1.recipe_id
                FROM Recipe r1 JOIN CookingToolsRequired t1 ON (r1.recipe_id = t1.recipe_id)
                    JOIN CookingTool t2 ON (t1.tool_id = t2.tool_id)
                WHERE t2.tool_name IN ({tools})'''.format(tools = input)
        if query == "":
            query += q
        else :
            query += (" INTERSECT " + q)

    restrictions = dietField.get()
    if(restrictions != ""):
        rst_lst = restrictions.split(",")
        input = str([i.lstrip().rstrip() for i in rst_lst])
        input = input[1:-1]
        q = '''SELECT DISTINCT r1.recipe_title, r1.recipe_id
                FROM Recipe r1 JOIN RecipeHasDietaryRestrictions d1 ON (r1.recipe_id = d1.recipe_id)
                    JOIN DietaryRestriction d2 ON (d1.restriction_id = d2.restriction_id)
                WHERE d2.restriction_name IN ({tools})'''.format(tools = input)
        if query == "":
            query += q
        else :
            query += (" INTERSECT " + q)

    cuisines = cuisineField.get()
    if(cuisines != ""):
        c_list = cuisines.split(",")
        input = str([c.lstrip().rstrip() for c in c_list])
        input = input[1:-1]
        q = '''SELECT recipe_title, recipe_id
                FROM Recipe
                WHERE cuisine_type IN ({cuisines})'''.format(cuisines = input)
        if query == "":
            query += q
        else :
            query += (" INTERSECT " + q)

    rs = con.cursor()
    rs.execute(query)
    result_window = tk.TopLevel(root)
    result_window.title("Results")

    recipeList = Listbox(result_window, width = 40)

    count = 0

    for (title, id) in rs:
        recipeList.insert(count, str(title))

    recipeList.pack()



searchButton = ttk.Button(recipeFrame, text="Search", command=search).grid(column=2, row=6)

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
