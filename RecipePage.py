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


class RecipePage:

    def __init__(self, master, user):
        self.myFrame = master

        usernameLabel = ttk.Label(self.myFrame, text="Enter usernames (separated by commas):").grid(column=1, row=1)
        self.usernameField = ttk.Entry(self.myFrame, width = 40)
        self.usernameField.grid(column=2, row = 1)

        IngredientLabel = ttk.Label(self.myFrame, text="Enter ingredients (separated by commas):").grid(column=1, row=2)
        self.IngredientField = ttk.Entry(self.myFrame, width = 40)
        self.IngredientField.grid(column=2, row = 2)

        toolLabel = ttk.Label(self.myFrame, text="Enter cooking tools (separated by commas):").grid(column=1, row=3)
        self.toolField = ttk.Entry(self.myFrame, width = 40)
        self.toolField.grid(column=2, row = 3)

        dietLabel = ttk.Label(self.myFrame, text="Enter dietary restrictions (separated by commas):").grid(column=1, row=4)
        self.dietField = ttk.Entry(self.myFrame, width = 40)
        self.dietField.grid(column=2, row = 4)

        cuisineLabel = ttk.Label(self.myFrame, text="Enter cuisine type (separated by commas):").grid(column=1, row=5)
        self.cuisineField = ttk.Entry(self.myFrame, width = 40)
        self.cuisineField.grid(column=2, row = 5)

        searchButton = ttk.Button(self.myFrame, text="Search", command=self.search).grid(column=1, row=6, columnspan=2)

    def search(self):
        query = ""

        usernames = self.usernameField.get()
        if(usernames != ""):
            users = usernames.split(",")
            usernameInput = str([u.lstrip().rstrip() for u in users])
            usernameInput = usernameInput[1:-1]
            q = '''SELECT r1.recipe_title, r1.recipe_id
                    FROM User u1 JOIN Recipe r1 ON (r1.username = u1.username)
                    WHERE u1.username IN ({users}) OR u1.name IN ({users})'''.format(users = usernameInput)
            query += q

        ingredients = self.IngredientField.get()
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

        tools = self.toolField.get()
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

        restrictions = self.dietField.get()
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

        cuisines = self.cuisineField.get()
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
        #result_window = tk.TopLevel(root)
        #result_window.title("Results")

        recipeList = Listbox(self.myFrame, width = 40)

        count = 0

        for (title, id) in rs:
            count += 1
            recipeList.insert(count, str(title))

        recipeList.grid(column = 1, row = 8, columnspan = 2)
