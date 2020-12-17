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
    ingredientIdList = []

    def __init__(self, user):
        self.myFrame = Tk()
        self.currUser = user
        self.myFrame.title("Add Recipe")
        self.myFrame.geometry("1000x600")
        #query to insert a recipe

        #recipe

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
        self.amountEntries = [Entry(ingredientFrame, width = 2) for i in range(15)]
        for i in range(15): self.amountEntries[i].grid(row=i+1, column = 4)

        unitLabels = [Label(ingredientFrame, text="Units:").grid(row=i+1, column = 5) for i in range(15)]
        self.unitEntries = [Entry(ingredientFrame, width = 4) for i in range(15)]
        for i in range(15): self.unitEntries[i].grid(row=i+1, column = 6)

        instructionFrame = LabelFrame(self.myFrame, text = "Instructions")
        instructionFrame.grid(row=2, column=2, rowspan = 2)

        instructionLabel = [Label(instructionFrame, text="Step " + str(i+1)+ ":").grid(row=i+1, column = 1) for i in range(10)]
        self.instructionEntries = [Entry(instructionFrame, width = 20) for i in range(10)]
        for i in range(10): self.instructionEntries[i].grid(row=i+1, column = 2, ipady=7)

        cookingToolFrame = LabelFrame(self.myFrame, text="Cooking Tools")
        cookingToolFrame.grid(row=2, column = 3)

        toolLabel = [Label(cookingToolFrame, text="Tool: " + str(i+1)+ ":", pady = 6).grid(row=i+1, column = 1) for i in range(6)]
        self.toolEntries = [Entry(cookingToolFrame, width = 25) for i in range(6)]
        for i in range(6): self.toolEntries[i].grid(row=i+1, column = 2)

        dietaryRestrictionFrame = LabelFrame(self.myFrame, text = "Dietary Restrictions")
        dietaryRestrictionFrame.grid(row=3, column = 3)

        restrictionLabel = [Label(dietaryRestrictionFrame, text="Restriction: " + str(i+1)+ ":", pady = 6).grid(row=i+1, column = 1) for i in range(6)]
        self.restrictionEntries = [Entry(dietaryRestrictionFrame, width = 20)for i in range(6)]
        for i in range(6): self.restrictionEntries[i].grid(row=i+1, column = 2)

        saveButton = Button(self.myFrame, text = "Save Recipe", command = self.save)
        saveButton.grid(row=4, column=1, columnspan = 3)

    def save(self):
        """ saves info """
        #currUser = None
        recipeTitle = self.recipeEntry.get()

        if(recipeTitle == ""):
            e = Error("Must provide a recipe name")
        cuisineType = self.cuisineEntry.get()
        foodType = self.foodEntry.get()

        recipeInfo = (foodType, cuisineType, recipeTitle, self.currUser)

        ingredientList = []
        for i in range(15):
            name = self.ingredientEntries[i].get()
            amount = self.amountEntries[i].get()
            unit = self.unitEntries[i].get()
            if(name != "" and amount != "" and unit != ""):
                ingredientList.append((name, amount, unit))

        if(len(ingredientList) == 0):
            e = Error("Must provide at least one ingredient")

        instructions = []
        for i in range(10):
            step = self.instructionEntries[i].get()
            if(step != ""):
                instructions.append((i+1, step))

        if(len(ingredientList) == 0):
            e = Error("Must provide at least one instruction")

        restrictions = []
        for i in range(6):
            restriction = self.restrictionEntries[i].get()
            if(restriction != ""):
                instructions.append(restriction)

        tools = []
        for i in range(6):
            tool = self.toolEntries[i].get()
            if(tool != ""):
                tools.append(tool)


        #format coming in
        #(food_type, cuisine_type, recipe_title, username)
        rs = con.cursor()
        #recipeInfo = ("pasta", "italian", "eu pasta", self.currUser)
        insert = '''INSERT INTO Recipe (food_type, cuisine_type, recipe_title, username)
                    VALUES ("{}","{}","{}","{}")'''.format(recipeInfo[0], recipeInfo[1], recipeInfo[2], recipeInfo[3])

        rs.execute(insert)
        con.commit()
        print("after insert and commit")
        #ingredientList = [("butter", 1, "cup"), ("salt", 1, "tbsp"), ("cinnamon", 2, "tbsp")]
        #query to insert a recipe
        #get recipe id
        getRecipeId = '''SELECT recipe_id FROM Recipe WHERE recipe_title = "{}"'''.format(recipeInfo[2])
        rs.execute(getRecipeId)
        recipeId = None
        for result in rs:
            print("get recipe id results",result)
            recipeId = result

        print(recipeId)
        ingredientList = [("parmesean", .5, "cups"), ("pasta", 1, "box"), ("marinara", 4, "cups"), ("salt", 2, "tsp")]
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
        #added instruction comments
        #instructions = [(1, "1i"),(2, "2i"),(3, "3i")]
        for instruction in instructions:
            insertInstruction = '''INSERT INTO Instruction (recipe_id, step_number, description)
                                        VALUES ({}, {}, "{}")'''.format(recipeId[0], instruction[0], instruction[1])
            rs.execute(insertInstruction)
            con.commit()
        
        #add dietary restrictions
        #restrictions.append("carnivore")
        #restrictions.append("omnivore")
        #restrictions =["r6", "r5", "vegan5"]
        for restriction in restrictions:
            searchQuery = '''SELECT restriction_id FROM DietaryRestriction WHERE LOWER(restriction_name) = LOWER("{}")'''.format(restrictions[0])
            rs.execute(searchQuery)
            row = rs.fetchone()
            print(row)
            if row is not None:
                print("dietary restriction already exists")
                '''insertRestrictionToRecipe = INSERT INTO RecipeHasDietaryRestrictions (recipe_id, restriction_id) 
                                                    VALUES ({}, {}).format(recipeId[0], row[0])
                rs.execute(insertRestrictionToRecipe)
                con.commit()'''
            else:
                insertRestrictionQuery = '''INSERT INTO DietaryRestriction (restriction_name)
                                                VALUES ("{}")'''.format(restrictions[0])
                rs.execute(insertRestrictionQuery)
                con.commit()

                searchQuery = '''SELECT restriction_id FROM DietaryRestriction WHERE LOWER(restriction_name) = LOWER("{}")'''.format(restrictions[0])
                rs.execute(searchQuery)
                restrictionId = rs.fetchone()

                insertRestrictionToRecipe = '''INSERT INTO RecipeHasDietaryRestrictions (recipe_id, restriction_id) 
                                                    VALUES ({}, {})'''.format(recipeId[0], restrictionId[0])
                rs.execute(insertRestrictionToRecipe)
                con.commit()


        tools = ["pot", "toaster", "knife"]
        for tool in tools:
            query = ''' SELECT tool_id
                        FROM CookingTool
                        WHERE LOWER(tool_name) = LOWER("{input}")'''.format(input = tool)
            rs.execute(query)
            index = rs.fetchone()
            if index is not None:
                index = index[0]
            else:
                query = '''INSERT INTO CookingTool (tool_name)
                           VALUES ("{input}")'''.format(input = tool)
                rs.execute(query)
                con.commit()
                query = ''' SELECT tool_id
                            FROM CookingTool
                            WHERE LOWER(tool_name) = LOWER("{input}")'''.format(input = tool)
                rs.execute(query)
                index = rs.fetchone()[0]
            query = ''' INSERT INTO CookingToolsRequired (tool_id,recipe_id)
                        VALUES ({input1}, {input2})'''.format(input1 = index, input2 = recipeId[0])
            rs.execute(query)
            con.commit()


            restrictions = ["vegan", "keto"]
            for restriction in restrictions:
                query = ''' SELECT restriction_id
                            FROM DietaryRestriction
                            WHERE LOWER(restriction_name) = LOWER("{input}")'''.format(input = restriction)
                rs.execute(query)
                index = rs.fetchone()
                if index is not None:
                    index = index[0]
                else:
                    query = '''INSERT INTO DietaryRestriction (restriction_name)
                               VALUES ("{input}")'''.format(input = restriction)
                    rs.execute(query)
                    con.commit()
                    query = ''' SELECT restriction_id
                                FROM DietaryRestriction
                                WHERE LOWER(restriction_name) = LOWER("{input}")'''.format(input = tool)
                    rs.execute(query)
                    index = rs.fetchone()
                    print(index)
                query = ''' INSERT INTO RecipeHasDietaryRestrictions (recipe_id, restriction_id)
                            VALUES ({input1}, {input2})'''.format(input1 = recipeId[0], input2 = index)
                #rs.execute(query)
                con.commit()

class Error:

    def __init__(self, errorMessage):
        self.myFrame = Tk()
        self.myFrame.title("Error")
        self.myFrame.geometry("300x100")

        errorLabel = Label(self.myFrame, text = errorMessage)
        errorLabel.grid(row=1, column=1, columnspan=3)

        okButton = Button(self.myFrame, text = "Ok", command = self.myFrame.destroy)
        okButton.grid(row=2, column=3)


class YourMeals:
    myFrame = None
    currUser = None

    def __init__(self, master, user):
        self.myFrame = master
        self.mealButton = ttk.Button(self.myFrame, text="Add Meal", command = self.addMeal)
        self.mealButton.grid(column = 1, row = 1)
        self.currUser = user

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

    def addMeal(self):
        """ TODO """
