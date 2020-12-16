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
    myFrame = None
    mealList = None
    mealName = None
    idList = []

    '''def go(self, event):
        print("here")
        mealName = self.mealList.get(mealList.curselection())
        print(mealName)'''

    def __init__(self, master, user):
        self.myFrame = master

        self.mealList = Listbox(self.myFrame, width = 40)
        rs = con.cursor()
        getMealNames = '''SELECT meal_name, meal_id
                            FROM Meal'''
        rs.execute(getMealNames)
        count = 0
        for meal, id in rs:
            self.idList.append(id)
            count += 1
            self.mealList.insert(count, str(meal))

        self.mealList.bind('<Double-1>', self.go)

        self.mealList.pack()

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
        for recipe_id in rs:
            print(recipe_id)
            self.idListArray.append(recipe_id[0])
            #count += 1
            #self.recipeList.insert(count, str(recipe_id[0]))

        for recipe_id in self.idListArray:
            rs = con.cursor()
            getRecipe = '''SELECT recipe_title, recipe_id
                            FROM Recipe
                            WHERE recipe_id = {}'''.format(recipe_id)
            rs.execute(getRecipe, (recipe_id))
            for recipe in rs:
                count +=1
                self.recipeList.insert(count, str(recipe))

        #do query to get the
        '''for recipe_id in idList:
            #get recipes information
            getRecipe = '''

        self.recipeList.pack()

    def go(self, event):

        # destroy everything in current frame so that recipe info can be built on top
        for widget in self.myFrame.winfo_children():
            widget.destroy()

        #r = DisplayMeal(myFrame, recipe_id)
