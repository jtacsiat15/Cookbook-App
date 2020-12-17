from tkinter import *

import mysql.connector
import sys
import config
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont

usr = config.mysql['user']
pwd = config.mysql['password']
hst = config.mysql['host']
dab = 'asmith37_DB'
# create a connection
con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

class ProfilePage:
    myFrame = None

    def __init__(self, master, user):
        self.myFrame = master
        recipeFrame = LabelFrame(self.myFrame, text="Your Recipes")
        recipeFrame.grid(column = 1, row=1)
        mealFrame = LabelFrame(self.myFrame, text ="Your Meals")
        mealFrame.grid(column = 2, row=1)
        currentUser = user

        r = YourRecipes(recipeFrame, user)
        m = YourMeals(mealFrame, user)


class YourRecipes:
    myFrame = None
    currUser = None
    def __init__(self, master, user):
        self.myFrame = master
        self.recipeLabel = ttk.Button(self.myFrame, text="Add Recipe", command=self.addRecipeFunction)
        self.recipeLabel.grid(column = 1, row = 1)
        self.currUser = user
        query = '''SELECT recipe_title, recipe_id
                    FROM Recipe
                    WHERE username = "{input}"'''.format(input = user)
        rs = con.cursor()
        rs.execute(query)
        self.recipeList = Listbox(self.myFrame, width = 40)

        count = 0
        for title, id in rs:
            count+=1
            self.recipeList.insert(count, title)

        self.recipeList.grid(column = 1, row = 2)

    def addRecipeFunction(self):
        addRecipe = AddRecipe(self.currUser)

class AddRecipe:
    myFrame = None
    currUser = None
    recipeEntry = None
    cuisineEntry = None
    foodEntry = None
    ingredientEntries = None
    amountEntries = None
    unitEntries = None
    instructionEntries = None
    restrictionEntries = None
    toolEntries = None

    def __init__(self, user):
        self.myFrame = Tk()
        self.currUser = user
        self.myFrame.title("Add Recipe")
        self.myFrame.geometry("1000x600")
        #recipe title

        recipeFrame = Frame(self.myFrame)
        recipeFrame.grid(row=1, column=1, columnspan = 3)

        recipeLabel = Label(recipeFrame, text="Recipe Name:")
        recipeLabel.grid(row=1, column=1)
        self.recipeEntry = Entry(recipeFrame, width = 40)
        self.recipeEntry.grid(row=1, column=2)

        cuisineLabel = Label(recipeFrame, text="Cuisine:")
        cuisineLabel.grid(row=2, column=1)
        self.cuisineEntry = Entry(recipeFrame, width = 40)
        self.cuisineEntry.grid(row=2, column=2)

        foodLabel = Label(recipeFrame, text="Food Type:")
        foodLabel.grid(row=3, column=1)
        self.foodEntry = Entry(recipeFrame, width = 40)
        self.foodEntry.grid(row=3, column=2)

        ingredientFrame = LabelFrame(self.myFrame, text = "Ingredients")
        ingredientFrame.grid(row=2, column=1, rowspan = 2)

        ingredientLabels = [Label(ingredientFrame, text=str(i+1)+": Ingredient Name:").grid(row=i+1, column = 1) for i in range(15)]
        self.ingredientEntries = [Entry(ingredientFrame, width = 10) for i in range(15)]
        for i in range(15): self.ingredientEntries[i].grid(row=i+1, column = 2)

        amountLabels = [Label(ingredientFrame, text="Amount:").grid(row=i+1, column = 3) for i in range(15)]
        self.amountEntries = [Entry(ingredientFrame, width = 2).grid(row=i+1, column = 4) for i in range(15)]
        unitLabels = [Label(ingredientFrame, text="Units:").grid(row=i+1, column = 5) for i in range(15)]
        self.unitEntries = [Entry(ingredientFrame, width = 4).grid(row=i+1, column = 6) for i in range(15)]

        instructionFrame = LabelFrame(self.myFrame, text = "Instructions")
        instructionFrame.grid(row=2, column=2, rowspan = 2)

        instructionLabel = [Label(instructionFrame, text="Step " + str(i+1)+ ":").grid(row=i+1, column = 1) for i in range(10)]
        self.instructionEntries = [Entry(instructionFrame, width = 20).grid(row=i+1, column = 2, ipady=7) for i in range(10)]

        cookingToolFrame = LabelFrame(self.myFrame, text="Cooking Tools")
        cookingToolFrame.grid(row=2, column = 3)

        toolLabel = [Label(cookingToolFrame, text="Tool: " + str(i+1)+ ":", pady = 5).grid(row=i+1, column = 1) for i in range(5)]
        self.toolEntries = [Entry(cookingToolFrame, width = 25).grid(row=i+1, column = 2) for i in range(5)]

        dietaryRestrictionFrame = LabelFrame(self.myFrame, text = "Dietary Restrictions")
        dietaryRestrictionFrame.grid(row=3, column = 3)

        restrictionLabel = [Label(dietaryRestrictionFrame, text="Restriction: " + str(i+1)+ ":", pady = 5).grid(row=i+1, column = 1) for i in range(8)]
        self.restrictionEntries = [Entry(dietaryRestrictionFrame, width = 20).grid(row=i+1, column = 2) for i in range(8)]

        saveButton = Button(self.myFrame, text = "Save Recipe", command = self.save)
        saveButton.grid(row=4, column=1, columnspan = 3)

    def save(self):
        """ saves info """
        #currUser = None
        recipeTitle = self.recipeEntry.get()
        cuisineType = self.cuisineEntry.get()
        foodType = self.foodEntry.get()

        ingredient = []
        for i in range(15):
            name = self.ingredientEntries[i].get()
            amount = self.amountEntries[i].get()
            unit = self.unitEntries[i].get()
            if(name != "" and amount != "" and unit != ""):
                ingredients.append((name, amount, unit))

        instructions = []

        instructionEntries = None
        restrictionEntries = None
        toolEntries = None
        """

class YourMeals:
    myFrame = None

    def __init__(self, master, user):
        self.myFrame = master
        self.mealButton = ttk.Button(self.myFrame, text="Add Meal")
        self.mealButton.grid(column = 1, row = 1)

        # query
        query = '''SELECT meal_name, meal_id
                    FROM Meal
                    WHERE username = "{input}"'''.format(input = user)
        rs = con.cursor()
        rs.execute(query)
        self.mealList = Listbox(self.myFrame, width = 40)

        count = 0
        for title, id in rs:
            count+=1
            self.mealList.insert(count, title)
        self.mealList.grid(column = 1, row = 2)
