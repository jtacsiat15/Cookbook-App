from tkinter import *

import mysql.connector
import sys
import config
from tkinter import ttk
import tkinter as tk
from RecipePage import DisplayRecipe
usr = config.mysql['user']
pwd = config.mysql['password']
hst = config.mysql['host']
dab = 'asmith37_DB'
# create a connection
con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

class MealPage:
    idList = []

    def go(self, event):
        print("here")
        mealName = self.mealList.get(mealList.curselection())
        print(mealName)

    def __init__(self, master, user):
        self.myFrame = master

        ratingLabel = ttk.Label(self.myFrame, text="Must have an average rating of at least: ").grid(column=1, row=1)
        self.ratingField = ttk.Entry(self.myFrame, width = 40)
        self.ratingField.grid(column=2, row = 1)

        foodLabel = ttk.Label(self.myFrame, text="Enter food types to include (separated by commas):").grid(column=1, row=2)
        self.foodField = ttk.Entry(self.myFrame, width = 40)
        self.foodField.grid(column=2, row = 2)

        dietFrame = Frame(self.myFrame)
        dietLabel1 = ttk.Label(dietFrame, text="Include at least").pack(side=LEFT)
        self.dietAmountField = ttk.Entry(dietFrame, width = 2)
        self.dietAmountField.pack(side=LEFT)
        dietLabel2 = ttk.Label(dietFrame, text="recipe(s) with dietary restriction: ").pack(side=LEFT)
        dietFrame.grid(column=1, row=3)
        self.dietField = ttk.Entry(self.myFrame, width = 40)
        self.dietField.grid(column=2, row = 3)

        cuisineFrame = Frame(self.myFrame)
        cuisineLabel1 = ttk.Label(cuisineFrame, text="Include at least").pack(side=LEFT)
        self.cuisineAmountField = ttk.Entry(cuisineFrame, width = 2)
        self.cuisineAmountField.pack(side=LEFT)
        cuisineLabel2 = ttk.Label(cuisineFrame, text="recipe(s) with cuisine type: ").pack(side=LEFT)
        cuisineFrame.grid(column=1, row=4)
        self.cuisineField = ttk.Entry(self.myFrame, width = 40)
        self.cuisineField.grid(column=2, row = 4)

        amountFrame = Frame(self.myFrame)
        recipeAmountLabel1 = ttk.Label(amountFrame, text="Number of recipes in meal must be between").pack(side=LEFT)
        self.recipeMinField = ttk.Entry(amountFrame, width = 2)
        self.recipeMinField.pack(side=LEFT)
        cuisineLabel2 = ttk.Label(amountFrame, text="and").pack(side=LEFT)
        self.recipeMaxField = ttk.Entry(amountFrame, width = 2)
        self.recipeMaxField.pack(side=LEFT)
        amountFrame.grid(column=1, row=5)


        usernameLabel = ttk.Label(self.myFrame, text="Recipes in meal must be made by (enter users, separated by commas):").grid(column=1, row=6)
        self.usernameField = ttk.Entry(self.myFrame, width = 40)
        self.usernameField.grid(column=2, row = 6)

        searchButton = ttk.Button(self.myFrame, text="Search", command=self.search).grid(column=1, row=7, columnspan=2)

    def search(self):
        query = '''SELECT meal_name, meal_id
                    FROM Meal'''

        averageRating = self.ratingField.get()
        if(averageRating != "" and self.isFloat(averageRating)):
            q = '''SELECT m.meal_name, m.meal_id
                    FROM Meal m JOIN RecipesInMeals rm ON (m.meal_id = rm.meal_id)
                    JOIN Rating r ON (r.recipe_id = rm.recipe_id)
                    HAVING AVG(r.score) > {input};'''.format(input = float(averageRating))
            query += (" INTERSECT " + q)


        food = self.foodField.get()
        if(food != ""):
            foodlst = food.split(",")
            fInput = str([f.lstrip().rstrip() for f in foodlst])
            fInput = fInput[1:-1]
            q = '''SELECT DISTINCT m.meal_name, m.meal_id
                    FROM Meal m JOIN RecipesInMeals rm ON (m.meal_id = rm.meal_id)
                        JOIN Recipe r ON (rm.recipe_id = r.recipe_id)
                    WHERE r.food_type IN ({input});'''.format(input = fInput)
            query += (" INTERSECT " + q)

        dietAmount = self.dietAmountField.get()
        diet = self.dietField.get()
        if(dietAmount != "" and self.isFloat(dietAmount) and diet != ""):
            q = '''SELECT DISTINCT m.meal_name, m.meal_id
                    FROM Meal m JOIN RecipesInMeals rm ON (m.meal_id = rm.meal_id)
                      JOIN RecipeHasDietaryRestrictions rd ON (rm.recipe_id = rd.recipe_id)
                      JOIN DietaryRestriction d ON (d.restriction_id = rd.restriction_id)
                    WHERE d.restriction_name = "{input1}"
                    GROUP BY m.meal_id
                      HAVING COUNT(*) >= {input2}'''.format(input1 = diet, input2 = float(dietAmount))
            query += (" INTERSECT " + q)

        cuisineAmount = self.cuisineAmountField.get()
        cuisine = self.cuisineField.get()
        if(cuisineAmount != "" and self.isFloat(cuisineAmount) and cuisine != ""):
            q = '''SELECT DISTINCT m.meal_name, m.meal_id
                    FROM Meal m JOIN RecipesInMeals rm ON (m.meal_id = rm.meal_id)
                      JOIN Recipe r ON (rm.recipe_id = r.recipe_id)
                    WHERE LOWER(r.cuisine_type) = "{input1}"
                    GROUP BY m.meal_id
                      HAVING COUNT(*) >= {input2}'''.format(input1 = cuisine, input2 = float(cuisineAmount))
            query += (" INTERSECT " + q)

        recipeAmount1 = self.recipeMinField.get()
        recipeAmount2 = self.recipeMaxField.get()

        if(recipeAmount1 != '' and recipeAmount2 != '' and self.isFloat(recipeAmount1) and self.isFloat(recipeAmount1)):
            q = '''SELECT DISTINCT m.meal_name, m.meal_id
                    FROM Meal m JOIN RecipesInMeals rm ON (m.meal_id = rm.meal_id)
                    GROUP BY m.meal_id
                    HAVING COUNT(*) >= {input1} AND COUNT(*) <= {input2}'''.format(input1 = float(recipeAmount1), input2 = float(recipeAmount2))
            query += (" INTERSECT " + q)
            print(q)

        rs = con.cursor()
        rs.execute(query)

        self.mealList = Listbox(self.myFrame, width = 40)
        count = 0
        for meal, id in rs:
            self.idList.append(id)
            count += 1
            self.mealList.insert(count, str(meal))

        self.mealList.bind('<Double-1>', self.go)

        self.mealList.grid(column=1, row = 8)

    def go(self, event):
        print("here in meal doubleClick")

        id_index = self.mealList.curselection()[0]
        meal_id = self.idList[id_index]

        print(meal_id)
        #print(mealName)
        d = DisplayMeal(meal_id)

    def isFloat(self, s):
        """ helper function """
        try:
            float(s)
            return True
        except ValueError:
            return False

class DisplayMeal:
    myFrame = None
    # meal info to be displayed
    recipeList = None
    idListArray = []
    recipeIdList = []
    recipe_id = None

    def __init__(self, meal_id):
        rs = con.cursor()
        
        self.myFrame = Tk()
        self.myFrame.title("Meal")
        self.myFrame.geometry("350x350")
        print(meal_id)
        self.recipeList = Listbox(self.myFrame, width = 40)
        getMealInfo = "SELECT meal_name, description WHERE meal_id = {}".format(meal_id)
        rs.execute(getMealInfo)
        for mealInfo in rs:
            mealName =  Label(self.myFrame, text = mealInfo[0])
            mealName.pack
            mealDescription = Label(self.myFrame, text = mealInfo[1])
            mealDescription.pack()


        
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
        self.recipeIdList.clear()
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
                self.recipeIdList.append(recipe[1])
                self.recipeList.insert(count, str(recipe[0]))
        #do query to get the
        '''for recipe_id in idList:
            #get recipes information
            getRecipe = '''
        print(self.recipeList.size())
        #id_index = self.mealList.curselection()[0]
        #id_index = self.recipeList.curselection()[0]
        #print("id index", id_index)
        #self.recipe_id = self.idList[id_index]
        self.recipeList.bind('<Double-1>', self.go)
        self.recipeList.pack()


    def go(self, event):
        print("display recipe meals")
        id_index = self.recipeList.curselection()[0]
        print(id_index)
        d = DisplayRecipe(self.recipeIdList[id_index])
        # destroy everything in current frame so that recipe info can be built on top
        #for widget in self.myFrame.winfo_children():
        #    widget.destroy()

        #r = DisplayMeal(myFrame, recipe_id)
