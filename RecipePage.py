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
    myFrame = None
    usernameField = None
    IngredientField = None
    toolField = None
    dietField = None
    cuisineField = None
    recipeIDList = []
    recipeList = None
    ingredientAmountField = None
    cuisineIngredientField = None

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

        ingredientFrame = Frame(self.myFrame)
        ingredientLabel1 = ttk.Label(ingredientFrame, text="Must include top 3 ingredients of cuisine: ").pack(side=LEFT)
        ingredientFrame.grid(column=1, row=6)
        self.cuisineIngredientField = ttk.Entry(self.myFrame, width = 40)
        self.cuisineIngredientField.grid(column=2, row = 6)

        searchButton = ttk.Button(self.myFrame, text="Search", command=self.search).grid(column=1, row=7, columnspan=2)

    def search(self):
        self.recipeIDList = []
        self.recipeList = Listbox(self.myFrame, width = 40)

        query = '''SELECT r1.recipe_title, r1.recipe_id
                    FROM Recipe r1 '''

        usernames = self.usernameField.get()
        if(usernames != ""):
            users = usernames.split(",")
            usernameInput = str([u.lstrip().rstrip() for u in users])
            usernameInput = usernameInput[1:-1]
            q = '''SELECT r1.recipe_title, r1.recipe_id
                    FROM User u1 JOIN Recipe r1 ON (r1.username = u1.username)
                    WHERE u1.username IN ({users}) OR u1.name IN ({users})'''.format(users = usernameInput)
            query += (" INTERSECT " + q)

        ingredients = self.IngredientField.get()
        if(ingredients != ""):
            ing_lst = ingredients.split(",")
            input = str([i.lstrip().rstrip() for i in ing_lst])
            input = input[1:-1]
            q = '''SELECT DISTINCT r1.recipe_title, r1.recipe_id
                    FROM Recipe r1 JOIN IngredientOf i1 ON (r1.recipe_id = i1.recipe_id)
                        JOIN Ingredient i2 ON (i1.ingredient_id = i2.ingredient_id)
                    WHERE i2.ingredient_name IN ({ingredients})'''.format(ingredients = input)
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
            query += (" INTERSECT " + q)

        cuisines = self.cuisineField.get()
        if(cuisines != ""):
            c_list = cuisines.split(",")
            input = str([c.lstrip().rstrip() for c in c_list])
            input = input[1:-1]
            q = '''SELECT recipe_title, recipe_id
                    FROM Recipe
                    WHERE cuisine_type IN ({cuisines})'''.format(cuisines = input)
            query += (" INTERSECT " + q)

        subquery = '''SELECT r.recipe_title, r.recipe_id
                    FROM AvgRating a JOIN ({input}) r ON (a.recipe_id = r.recipe_id)
                    ORDER BY a.avg_score DESC
                    LIMIT 20'''.format(input = query)

        rs = con.cursor()
        rs.execute(subquery)

        self.recipeList.bind('<Double-1>', self.go)
        count = 0

        for (title, id) in rs:
            count += 1
            print(title)
            print(id)
            self.recipeIDList.append(id)
            self.recipeList.insert(count, str(title))

        self.recipeList.grid(column = 1, row = 8, columnspan = 2)

    def go(self, event):
        index = self.recipeList.curselection()[0]
        recipe_id = self.recipeIDList[index]
        print(recipe_id)
        displayRecipe = DisplayRecipe(recipe_id)

class DisplayRecipe:
    def __init__(self, recipe_id):
        self.myFrame = Tk()
        self.myFrame.title("Recipe")
        self.myFrame.geometry("700x700")
        ingredientList = Listbox(self.myFrame, width = 100)
        instructionsList = Listbox(self.myFrame, width = 100)

        #display ingredients
        rs = con.cursor()


        query = '''SELECT recipe_title, cuisine_type, food_type
                    FROM Recipe
                    WHERE recipe_id = {}'''.format(recipe_id)

        rs.execute(query)
        for info in rs:
            title = Label(self.myFrame, text = info[0])
            title.pack()
            description = Label(self.myFrame, text = "Cuisine: " + str(info[1]))
            description.pack()
            desc2 = Label(self.myFrame, text = "Food: " + str(info[2]))
            desc2.pack()

        query = ''' SELECT avg_score
                    FROM AvgRating WHERE recipe_id = {}'''.format(recipe_id)

        rs.execute(query)
        for info in rs:
            rating = Label(self.myFrame, text = "Average Rating: " + str(info[0])[:-3])
            rating.pack()

        query = '''SELECT d.restriction_name
                    FROM Recipe r JOIN RecipeHasDietaryRestrictions hr ON (r.recipe_id = hr.recipe_id)
                                    JOIN DietaryRestriction d ON (hr.restriction_id = d.restriction_id)
                    WHERE r.recipe_id = {}'''.format(recipe_id)

        infoFrame = Frame(self.myFrame)
        restrictionList = Listbox(infoFrame, width = 20, height = 5)
        toolList = Listbox(infoFrame, width = 20, height = 5)

        rs.execute(query)
        restrictionCount = 0
        for restriction in rs:
            restrictionCount += 1
            restrictionList.insert(restrictionCount, restriction)
        restrictionList.grid(column = 1, row = 1)
        query = '''SELECT d.tool_name
                    FROM Recipe r JOIN CookingToolsRequired cr ON (r.recipe_id = cr.recipe_id)
                                    JOIN CookingTool d ON (cr.tool_id = d.tool_id)
                    WHERE r.recipe_id = {}'''.format(recipe_id)

        rs.execute(query)
        toolCount = 0
        for tool in rs:
            toolCount += 1
            toolList.insert(toolCount, tool)
        toolList.grid(column = 2, row = 1)

        infoFrame.pack()

        getRecipeIngredients = '''SELECT i.ingredient_name, io.amount, io.measurement_units
                                    FROM IngredientOf io JOIN Ingredient i USING (ingredient_id)
                                    WHERE io.recipe_id = {}'''.format(recipe_id)
        rs.execute(getRecipeIngredients)
        count = 0
        for ingredients in rs:
            count += 1
            ingredientList.insert(count, ingredients)
        ingredientList.pack()

        getInstructions = '''SELECT step_number, description
                                FROM Instruction
                                WHERE recipe_id = {}'''.format(recipe_id)
        rs.execute(getInstructions)

        instructionCount = 0
        for instruction in rs:
            instructionCount += 1
            instructionsList.insert(instructionCount, instruction)
        instructionsList.pack()
22
