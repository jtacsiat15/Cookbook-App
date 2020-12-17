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
    ingredientIdList = []
    def __init__(self, user):
        self.myFrame = Tk()
        self.currUser = user
        self.myFrame.title("Add Recipe")
        self.myFrame.geometry("350x350")
        #query to insert a recipe
        #format coming in
        #(food_type, cuisine_type, recipe_title, username)
        rs = con.cursor()
        recipeTest = ("pasta", "italian", "eu pasta", self.currUser)
        insert = '''INSERT INTO Recipe (food_type, cuisine_type, recipe_title, username) 
                    VALUES ("{}","{}","{}","{}")'''.format(recipeTest[0], recipeTest[1], recipeTest[2], recipeTest[3])
        
        rs.execute(insert)
        con.commit()
        print("after insert and commit")
        ingredientList = [("butter", 1, "cup"), ("salt", 1, "tbsp"), ("cinnamon", 2, "tbsp")]
        #query to insert a recipe
        #get recipe id 
        getRecipeId = '''SELECT recipe_id FROM Recipe WHERE recipe_title = "{}"'''.format(recipeTest[2])
        rs.execute(getRecipeId)
        recipeId = None
        for result in rs:
            print("get recipe id results",result)
            recipeId = result
    
        print(recipeId)
        for ingredient in ingredientList:
            searchQuery = '''SELECT ingredient_id FROM Ingredient WHERE LOWER(ingredient_name) = LOWER("{}")'''.format(ingredient[0])
            rs.execute(searchQuery)
            print("past query")
            row = rs.fetchone()
            print(row)
            if row is not None:
                print("ingredient already exist")
                self.ingredientIdList.append(row[0])
                insertIngredientDetails = '''INSERT INTO IngredientOf (recipe_id, ingredient_id, amount, measurement_units) 
                                                 VALUES ({}, {}, {}, "{}")'''.format(recipeId[0], row[0], ingredient[1], ingredient[2])
                print(insertIngredientDetails)
                rs.execute(insertIngredientDetails)
                con.commit()
            else:
                print("in ingredient else")
                #insert into ingredient 
                insertIngredient = '''INSERT INTO Ingredient (ingredient_name) VALUES ("{}")'''.format(ingredient[0])
                rs.execute(insertIngredient)
                searchQuery = '''SELECT ingredient_id FROM Ingredient WHERE LOWER(ingredient_name) = LOWER("{}")'''.format(ingredient[0])
                rs.execute(searchQuery)
                row = rs.fetchone()
                print("ingredient id", row[0])
                #self.ingredientIdList.append(row[0])
                print("past insert query")
                #insert ingredient into recipe
                insertIngredientDetails = '''INSERT INTO IngredientOf (recipe_id, ingredient_id, amount, measurement_units) 
                                                 VALUES ({}, {}, {}, "{}")'''.format(recipeId[0], row[0], ingredient[1], ingredient[2])
                print(insertIngredientDetails)
                rs.execute(insertIngredientDetails)
                con.commit()
        print("after for ingredient loop")
        #for ingredient_id in ingredientIdList:
        #code to add instructions
        
            


        #recipe 



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

