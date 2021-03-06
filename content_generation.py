

import random


def values(count, num, instructions, measurements, usernames):
    cnt_common = random.sample(range(0, 12), random.randint(1,6))
    cnt_s = random.sample(range(0, 9), random.randint(1,9))
    for c in cnt_common:
        ingredientOfquery = ("("+ str(count) + ", " + str(71 + c) + ", " + str(random.randint(1,10)) + ", \"" + str(measurements[random.randint(0,2)])+ "\"),\n")
    for c in cnt_s:
        ingredientOfquery += ("(" + str(count) + ", " + str(num + c) + ", " + str(random.randint(1,10)) + ", \"" + str(measurements[random.randint(0,2)])+ "\"),\n")
    cnt_tools = random.sample(range(1,15), random.randint(1,14))
    toolsquery = ""
    for c in cnt_tools:
        toolsquery += ("(" + str(c) + ", " + str(count) + "),\n")
    cnt_restr = random.sample(range(1,10), random.randint(1,7))
    restrquery = ""
    for c in cnt_restr:
        if c < 6:
            restrquery = ("(" + str(count) + ", " + str(c) + "),\n")

    reviewsquery = ""
    scores = []
    for i in range(30):
        rnge = random.randint(1,3)
        if rnge == 3:
            scores.append(random.randint(4,5))
        elif rnge == 2:
            scores.append(random.randint(3,5))
        else:
            scores.append(random.randint(1,4))
    year = [random.randint(2005, 2020) for i in range(30)]
    month = [random.randint(1, 12) for i in range(30)]
    day = [random.randint(1, 28) for i in range(30)]
    for i in range(30):
        reviewsquery = "(" + str(scores[i]) + ", \"" + str(year[i]) + "-" + str(month[i])+ "-" + str(day[i]) + "\", \"" + str(usernames[random.randint(0, len(usernames)-1)]) + "\", " + str(count) + "),\n"
    cnt_steps = random.sample(range(0, 12), random.randint(1, 10))
    instructionsquery = ""
    for i in range(len(cnt_steps)):
        instructionsquery += "("+ str(count) + ", " + str(i+1) + ", \"" + instructions[cnt_steps[i]] + "\"),\n"
    return ingredientOfquery, toolsquery, restrquery, reviewsquery, instructionsquery

def generateValues(fout):
    """ outputs an insert statements for amount statement to specified file """

    query = "INSERT INTO DietaryRestriction (restriction_name) \n VALUES "
    restrictions = ["Vegan", "Vegetarian", "Lactose Intolerant", "Gluten Free", "Keto", "Pescatarian"]

    for r in restrictions: query += "(\"" + r + "\"),\n"
    query = query[:-2] + ";\n\n"
    fout.write(query)

    query = "INSERT INTO CookingTool (tool_name) \n VALUES "
    cookingTools = ["Air Fryer", "Convection Oven", "Microwave", "Rice Cooker", "Popcorn Machine", "Spoons", "Pot", "Saucepan", "Large Bowl", "Standing Mixer", "Stovetop", "Oven", "Toaster", "Blender", "Grill"]
    for c in cookingTools: query += "(\"" + c + "\"),\n"
    query = query[:-2] + ";\n\n"
    fout.write(query)

    firstnames = ["Anna","Jalen","Ayisha","Nida","Cara","Ellise","Dominika","Samara","Addison","Amayah"]
    lastnames = ["Rivers","Whittington","Macias","Alvarez","Edwards","Franks","Riggs","Stott","Howe","Appleton","Kaur","Mercer","Rios","Hook","Blundell"]
    names = []
    for l in lastnames:
        for f in firstnames:
            names.append(f + " " + l)


    usernames = ["chef_" + firstnames[i%10].lower() + str(i) for i in range(100)]
    password = "ilovetocook123!"

    query = "INSERT INTO User (username, name, password)\n VALUES "
    for i in range(100):
        query+= "(\"" + usernames[i] + "\", \"" + names[i]+ "\", \"" + password + "\"),\n"
    query = query[:-2] + ";\n\n"
    fout.write(query)

    common = ["Eggs", "Garlic", "Chicken", "Pork", "Beef", "Tomato", "Lettuce", "Rice", "Sugar", "Flour", "Water", "Milk"]
    japanese = ["Ginger", "Salt", "Mirin", "Wasabi", "Nori", "Rice Vinegar", "Miso", "Noodles", "Green Onion", "Soy Sauce"]
    chinese = ["Oyster Sauce", "Cabbage", "Scallions", "Chinese Soy Sauce", "Ground Pork", "Chili Paste", "Star Anise", "Shitake Mushrooms", "Plum Sauce", "Sesame Oil"]
    italian = ["Basil", "Red Wine", "Pasta", "Balsamic Vinegar", "Raviolli,", "Mozzarella", "Oregano","Mushrooms", "Parmesean", "Ricotta"]
    indian = ["Cloves", "Lentils", "Coriander", "Chickpeas", "Cinnamon", "Saffron", "Cardamom", "Tofu", "Garam Masala", "Coconut"]
    vietnamese = ["Rice Noodles", "Fish Sauce", "Hoisin", "Lemongrass", "Jasmine Rice", "Shrimp Paste", "Shallots", "Thai Basil", "Lemon", "Turmeric"]
    mexican = ["Black Beans", "Corn", "Jalepenos", "Avocados", "Lime", "Tortillas", "Chorizo", "Cilantro", "Pinto Beans", "White Beans"]
    american = ["Oil", "Bacon", "Butter", "Cereal", "Pancake Mix", "White Bread", "Twinkies", "Jell-o", "American Cheese", "Potato Chips"]

    japaneseRange = [1, 10]
    chineseRange = [11, 20]
    italianRange = [21, 30]
    indianRange = [31, 40]
    vietnameseRange = [41, 50]
    mexicanRange = [51, 60]
    americanRange = [61, 70]

    query = "INSERT INTO Recipe (food_type, cuisine_type, recipe_title, username)\n VALUES "

    japaneseFoods = ["Sushi", "Miso Soup", "Tonkotsu Ramen", "Onigiri", "Tempura", "Soba Noodles", "Udon Noodles"]
    chineseFoods = ["Wonton Soup", "Orange Chicken", "Sesame Chicken", "Sweet and Sour Pork", "Kung Pao Chicken", "Potstickers"]
    italianFoods = ["Risotto", "Lasagne", "Linguine", "Alfredo", "Cannoli", "Breadsticks"]
    americanFoods = ["Meatloaf", "Mashed Potatoes", "Macaroni and Cheese", "Deep Fried Oreos", "Chicken Wings", "Scrambled Eggs", "Cereal"]
    indianFoods = ["Samosa", "Butter Chicken", "Tandoori Chicken", "Tikka Masala", "Dosas"]
    vietnameseFoods = ["Pho", "Bahn Mi", "Spring Rolls", "Lemongrass Chicken", "Spicy Beef Soup"]
    mexicanFoods = ["Tacos", "Enchiladas", "Burritos", "Quesadillas", "Taquitos"]


    cuisines = []
    cuisines.extend(japanese)
    cuisines.extend(chinese)
    cuisines.extend(italian)
    cuisines.extend(indian)
    cuisines.extend(vietnamese)
    cuisines.extend(mexican)
    cuisines.extend(american)
    cuisines.extend(common)

    numbered_cuisines = []

    query = "INSERT INTO Ingredient (ingredient_name, recipe_id)\n VALUES "
    for c in cuisines:
        query+= "(\""+c+"\", NULL),\n"
    query = query[:-2] + ";\n\n"
    fout.write(query)

    titles = ["World's Best ", "Grandma's ", "Delicious ", "Award-Winning ","Quick and Easy ", "Wonderful ", "Amazing ", "Tasty ", "Healthy ", "Perfect ", "Quick ", "Easy ", "Simple ", "Traditional ", "Classic ", "Unhealthy ", "Authentic ", "The Best ", "Spectacular ", "Mouth-Watering ", "Savory ", "Sweet ", "Fancy ", "Flavorful ", "Delectable "]

    measurements = ["cups", "tablespoons", "teaspoons"]

    count = 1
    ingredientOfquery = "INSERT INTO IngredientOf (recipe_id, ingredient_id, amount, measurement_units)\n VALUES "
    query = "INSERT INTO Recipe (food_type, cuisine_type, recipe_title, username)\n VALUES "
    toolsquery = "INSERT INTO CookingToolsRequired (tool_id, recipe_id)\n VALUES "
    restrquery = "INSERT INTO RecipeHasDietaryRestrictions (recipe_id, restriction_id)\n VALUES "
    reviewsquery = "INSERT INTO Rating (score, date_added, username, recipe_id)\n VALUES "

    instructions = ["Preheat oven to 350 degrees", "In a large bowl, combine ingredients", "Let sit for 1 hour", "Add a pinch of salt", "Bring to a boil, and cook for 10-15 minutes", "Prepare ingredients", "Let cool", "Whisk together dry ingredients", "Marinate for 1 hour", "Place ingredients into blender and blend for 1-2 minutes", "Mix on high speed for 3-5 minutes", "Bake for 20-30 minutes", "rotating half-way through"]
    instructionsquery = "INSERT INTO Instruction (recipe_id, step_number, description)\n VALUES "

    for j in japaneseFoods:
        for t in titles:
            query+= "(\"" + j + "\", \"Japanese\", \"" + t + j + "\", \"" + usernames[random.randint(0, len(usernames)-1)]+"\"),\n"
            ingredient, tools, restr, reviews, instr = values(count, 1, instructions, measurements, usernames)
            ingredientOfquery += ingredient
            toolsquery += tools
            restrquery += restr
            reviewsquery += reviews
            instructionsquery += instr
            count += 1
    for j in chineseFoods:
        for t in titles:
            query+= "(\""+j+"\", \"Chinese\", \"" + t + j + "\", \"" + usernames[random.randint(0, len(usernames)-1)]+"\"),\n"
            ingredient, tools, restr, reviews, instr = values(count, 11, instructions, measurements, usernames)
            ingredientOfquery += ingredient
            toolsquery += tools
            restrquery += restr
            reviewsquery += reviews
            instructionsquery += instr
            count += 1
    for j in italianFoods:
        for t in titles:
            query+= "(\""+j+"\", \"Italian\", \"" + t + j + "\", \"" + usernames[random.randint(0, len(usernames)- 1)]+"\"),\n"
            ingredient, tools, restr, reviews, instr = values(count, 21, instructions, measurements, usernames)
            ingredientOfquery += ingredient
            toolsquery += tools
            restrquery += restr
            reviewsquery += reviews
            instructionsquery += instr
            count += 1
    for j in americanFoods:
        for t in titles:
            query+= "(\""+j+"\", \"American\", \"" + t + j + "\", \"" + usernames[random.randint(0, len(usernames) - 1)]+"\"),\n"
            ingredient, tools, restr, reviews, instr = values(count, 61, instructions, measurements, usernames)
            ingredientOfquery += ingredient
            toolsquery += tools
            restrquery += restr
            reviewsquery += reviews
            instructionsquery += instr
            count += 1
    for j in indianFoods:
        for t in titles:
            query+= "(\""+j+"\", \"Indian\", \"" + t + j + "\", \"" + usernames[random.randint(0, len(usernames) - 1)] + "\"),\n"
            ingredient, tools, restr, reviews, instr = values(count, 31, instructions, measurements, usernames)
            ingredientOfquery += ingredient
            toolsquery += tools
            restrquery += restr
            reviewsquery += reviews
            instructionsquery += instr
            count += 1
    for j in vietnameseFoods:
        for t in titles:
            query+= "(\""+j+"\", \"Vietnamese\", \"" + t + j + "\", \"" + usernames[random.randint(0, len(usernames) - 1)]+ "\"),\n"
            ingredient, tools, restr, reviews, instr = values(count, 41, instructions, measurements, usernames)
            ingredientOfquery += ingredient
            toolsquery += tools
            restrquery += restr
            reviewsquery += reviews
            instructionsquery += instr
            count += 1
    for j in mexicanFoods:
        for t in titles:
            query+= "(\""+j+"\", \"Mexican\", \"" + t + j + "\", \"" + usernames[random.randint(0, len(usernames) - 1)] + "\"),\n"
            ingredient, tools, restr, reviews, instr = values(count, 51, instructions, measurements, usernames)
            ingredientOfquery += ingredient
            toolsquery += tools
            restrquery += restr
            reviewsquery += reviews
            instructionsquery += instr
            count += 1

    query = query[:-2] + ";\n\n"
    fout.write(query)

    ingredientOfquery = ingredientOfquery[:-2] + ";\n\n"
    fout.write(ingredientOfquery)

    toolsquery = toolsquery[:-2] + ";\n\n"
    fout.write(toolsquery)

    restrquery = restrquery[:-2] + ";\n\n"
    fout.write(restrquery)

    reviewsquery = reviewsquery[:-2] + ";\n\n"
    fout.write(reviewsquery)

    instructionsquery = instructionsquery[:-2] + ";\n\n"
    fout.write(instructionsquery)
    count = count -1

    mealquery = "INSERT INTO Meal(meal_name, description, username) \nVALUES "
    mrquery = "INSERT INTO RecipesInMeals (recipe_id, meal_id) \n VALUES "

    descritions = ["A delicious meal", "Very simple weeknight meal", "A meal to impress guests", "A healthy dinner", "The best thanksgivin meals", "My favorite recipes of all time"]

    meal_count = 1
    for u in usernames:
        for i in range(random.randint(2, 15)):
            mealquery += "(\"My Meal " + str(i+1) + "\", \"" + descritions[random.randint(0, 5)] + "\", \"" + u + "\"),\n"
            cnt_recipes = random.sample(range(1, count), random.randint(1,8))
            for c in cnt_recipes:
                mrquery += "(" + str(c)+","+str(meal_count) + "),\n"
            meal_count += 1

    mealquery = mealquery[:-2] + ";\n\n"
    fout.write(mealquery)
    mrquery = mrquery[:-2] + ";\n\n"
    fout.write(mrquery)



def openFile(fname):
    """ opens file given file name """
    try:
        fout = open(fname, 'w')
    except FileNotFoundError:
        print("Error: File \"",fname,"\" Not Found");
        exit()

    return fout


def main():
    """ main function """

    # open file
    fout = openFile("project-data.sql")

    # generate values
    generateValues(fout)

    fout.close()

if __name__ == '__main__':
    main()
