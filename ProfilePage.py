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
    def __init__(self, user):
        self.myFrame = Tk()
        self.currUser = user
        self.myFrame.title("Add Recipe")
        self.myFrame.geometry("350x350")
        #recipe title



class YourMeals:
    myFrame = None

    def __init__(self, master, user):
        self.myFrame = master
        self.mealLabel = ttk.Button(self.myFrame, text="Add Meal")
        self.mealLabel.pack()

