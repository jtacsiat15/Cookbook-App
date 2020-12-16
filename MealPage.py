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

class MealPage:

    def go(self, event):
        print("here")
        mealName = self.mealList.get(mealList.curselection())
        print(mealName)

    def __init__(self, master, user):
        self.myFrame = master

        ratingLabel = ttk.Label(self.myFrame, text="Must have an average rating of: ").grid(column=1, row=1)
        self.ratingField = ttk.Entry(self.myFrame, width = 40).grid(column=2, row = 1)

        foodLabel = ttk.Label(self.myFrame, text="Enter food types to include (separated by commas):").grid(column=1, row=2)
        self.foodField = ttk.Entry(self.myFrame, width = 40).grid(column=2, row = 2)

        dietFrame = Frame(self.myFrame)
        dietLabel1 = ttk.Label(dietFrame, text="Include at least").pack(side=LEFT)
        self.dietAmountField = ttk.Entry(dietFrame, width = 2).pack(side=LEFT)
        dietLabel2 = ttk.Label(dietFrame, text="recipes with dietary restriction (separated by commas): ").pack(side=LEFT)
        dietFrame.grid(column=1, row=3)
        self.dietField = ttk.Entry(self.myFrame, width = 40).grid(column=2, row = 3)

        cuisineFrame = Frame(self.myFrame)
        cuisineLabel1 = ttk.Label(cuisineFrame, text="Include at least").pack(side=LEFT)
        self.cuisineAmountField = ttk.Entry(cuisineFrame, width = 2).pack(side=LEFT)
        cuisineLabel2 = ttk.Label(cuisineFrame, text="recipes with cuisine type (separated by commas): ").pack(side=LEFT)
        cuisineFrame.grid(column=1, row=4)
        self.cuisineField = ttk.Entry(self.myFrame, width = 40).grid(column=2, row = 4)

        amountFrame = Frame(self.myFrame)
        recipeAmountLabel1 = ttk.Label(amountFrame, text="Number of recipes in meal must be between").pack(side=LEFT)
        self.recipeMinField = ttk.Entry(amountFrame, width = 2).pack(side=LEFT)
        cuisineLabel2 = ttk.Label(amountFrame, text="and").pack(side=LEFT)
        self.recipeMaxField = ttk.Entry(amountFrame, width = 2).pack(side=LEFT)
        amountFrame.grid(column=1, row=5)

        usernameLabel = ttk.Label(self.myFrame, text="Recipes in meal must be made by (enter users, separated by commas):").grid(column=1, row=6)
        self.usernameField = ttk.Entry(self.myFrame, width = 40).grid(column=2, row = 6)

        searchButton = ttk.Button(self.myFrame, text="Search", command=self.search).grid(column=1, row=7, columnspan=2)
        
    def search(self):
        query = ""

        usernames = self.usernameField.get()
        if(usernames != ""):
            users = usernames.split(",")
            usernameInput = str([u.lstrip().rstrip() for u in users])
            usernameInput = usernameInput[1:-1]
            q = '''SELECT m1.meal_name, m1.meal_id
                    FROM User u1 JOIN Meal m1 ON (m1.username = m1.username)
                    WHERE u1.username IN ({users}) OR u1.name IN ({users})'''.format(users = usernameInput)
            query += q

        rs = con.cursor()
        rs.execute(query)

        self.mealList = Listbox(self.myFrame, width = 40)
        count = 0
        for meal, id in rs:
            self.idList.append(id)
            count += 1
            self.mealList.insert(count, str(meal))

        self.mealList.bind('<Double-1>', self.go)

        self.mealList.grid(column=2, row = 3)




    def go(self, event):
        print("here in meal doubleClick")

        id_index = self.mealList.curselection()[0]
        meal_id = self.idList[id_index]

        print(meal_id)
        #print(mealName)
        d = DisplayMeal(meal_id)




class DisplayMeal:
    myFrame = None
    # meal info to be displayed
    recipeList = None
    idListArray = []


    def __init__(self, meal_id):
        self.myFrame = Tk()
        self.myFrame.title("Meal")
        self.myFrame.geometry("350x350")
        print(meal_id)
        self.recipeList = Listbox(self.myFrame, width = 40)

        rs = con.cursor()
        # execute query to get meal info
        getRecipeIds = "SELECT recipe_id FROM RecipesInMeals WHERE meal_id = {}".format(meal_id)
        rs.execute(getRecipeIds, (meal_id))
        count = 0
        self.idListArray.clear()
        for recipe_id in rs:
            print(recipe_id)
            self.idListArray.append(recipe_id[0])
            #count += 1
            #self.recipeList.insert(count, str(recipe_id[0]))

        self.recipeList.delete(0, self.recipeList.size())
        print("past clear list")
        print(self.recipeList.size())
        for recipe_id in self.idListArray:
            rs = con.cursor()
            getRecipe = '''SELECT recipe_title, recipe_id
                            FROM Recipe
                            WHERE recipe_id = {}'''.format(recipe_id)
            rs.execute(getRecipe)
            for recipe in rs:
                count +=1
                self.recipeList.insert(count, str(recipe[0]))
        #do query to get the
        '''for recipe_id in idList:
            #get recipes information
            getRecipe = '''
        print(self.recipeList.size)
        self.recipeList.pack()


    def go(self, event):

        # destroy everything in current frame so that recipe info can be built on top
        for widget in self.myFrame.winfo_children():
            widget.destroy()

        #r = DisplayMeal(myFrame, recipe_id)
