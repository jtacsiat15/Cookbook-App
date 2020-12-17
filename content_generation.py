

import random

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

    for j in japaneseFoods:
        for t in titles:
            query+= "(\"" + j + "\", \"Japanese\", \"" + t + j + "\", \"" + usernames[random.randint(0, len(usernames)-1)]+"\"),\n"
            cnt_common = random.sample(range(0, 12), random.randint(1,6))
            cnt_s = random.sample(range(0, 9), random.randint(1,9))
            for c in cnt_common:
                ingredientOfquery += ("("+ str(count) + ", " + str(71 + c) + ", " + str(random.randint(1,10)) + ", \"" + str(measurements[random.randint(0,2)])+ "\"),\n")
            for c in cnt_s:
                ingredientOfquery += ("(" + str(count) + ", " + str(1 + c) + ", " + str(random.randint(1,10)) + ", \"" + str(measurements[random.randint(0,2)])+ "\"),\n")
            cnt_tools = random.sample(range(1,15), random.randint(1,14))
            for c in cnt_tools:
                toolsquery += ("(" + str(c) + ", " + str(count) + "),\n")
            cnt_restr = random.sample(range(1,10), random.randint(1,7))
            for c in cnt_restr:
                if c < 6:
                    restrquery += ("(" + str(count) + ", " + str(c) + "),\n")
            scores = [random.randint(1,5) for i in range (30)]
            year = [random.randint(2005, 2020) for i in range(30)]
            month = [random.randint(1, 12) for i in range(30)]
            day = [random.randint(1, 28) for i in range(30)]
            for i in range(30):
                reviewsquery += "(" + str(scores[i]) + ", \"" + str(year[i]) + "-" + str(month[i])+ "-" + str(day[i]) + "\", \"" + str(usernames[random.randint(0, len(usernames)-1)]) + "\", " + str(count) + "),\n"
            count += 1
    for j in chineseFoods:
        for t in titles:
            query+= "(\""+j+"\", \"Chinese\", \"" + t + j + "\", \"" + usernames[random.randint(0, len(usernames)-1)]+"\"),\n"
            cnt_common = random.sample(range(0, 12), random.randint(1,6))
            cnt_s = random.sample(range(0, 9), random.randint(1,9))
            for c in cnt_common:
                ingredientOfquery += ("("+ str(count) + ", " + str(71 + c) + ", " + str(random.randint(1,10)) + ", \"" + str(measurements[random.randint(0,2)])+ "\"),\n")
            for c in cnt_s:
                ingredientOfquery += ("(" + str(count) + ", " + str(11 + c) + ", " + str(random.randint(1,10)) + ", \"" + str(measurements[random.randint(0,2)])+ "\"),\n")
            cnt_tools = random.sample(range(1,15), random.randint(1,14))
            for c in cnt_tools:
                toolsquery += ("(" + str(c) + ", " + str(count) + "),\n")
            cnt_restr = random.sample(range(1,10), random.randint(1,7))
            for c in cnt_restr:
                if c < 6:
                    restrquery += ("(" + str(count) + ", " + str(c) + "),\n")
            scores = [random.randint(1,5) for i in range (30)]
            year = [random.randint(2005, 2020) for i in range(30)]
            month = [random.randint(1, 12) for i in range(30)]
            day = [random.randint(1, 28) for i in range(30)]
            for i in range(30):
                reviewsquery += "(" + str(scores[i]) + ", \"" + str(year[i]) + "-" + str(month[i])+ "-" + str(day[i]) + "\", \"" + str(usernames[random.randint(0, len(usernames)-1)]) + "\", " + str(count) + "),\n"
            count += 1
    for j in italianFoods:
        for t in titles:
            query+= "(\""+j+"\", \"Italian\", \"" + t + j + "\", \"" + usernames[random.randint(0, len(usernames)- 1)]+"\"),\n"
            cnt_common = random.sample(range(0, 12), random.randint(1,6))
            cnt_s = random.sample(range(0, 9), random.randint(1,9))
            for c in cnt_common:
                ingredientOfquery += ("("+ str(count) + ", " + str(71 + c) + ", " + str(random.randint(1,10)) + ", \"" + str(measurements[random.randint(0,2)])+ "\"),\n")
            for c in cnt_s:
                ingredientOfquery += ("(" + str(count) + ", " + str(21 + c) + ", " + str(random.randint(1,10)) + ", \"" + str(measurements[random.randint(0,2)])+ "\"),\n")
            cnt_tools = random.sample(range(1,15), random.randint(1,14))
            for c in cnt_tools:
                toolsquery += ("(" + str(c) + ", " + str(count) + "),\n")
            cnt_restr = random.sample(range(1,10), random.randint(1,7))
            for c in cnt_restr:
                if c < 6:
                    restrquery += ("(" + str(count) + ", " + str(c) + "),\n")
            scores = [random.randint(1,5) for i in range (30)]
            year = [random.randint(2005, 2020) for i in range(30)]
            month = [random.randint(1, 12) for i in range(30)]
            day = [random.randint(1, 28) for i in range(30)]
            for i in range(30):
                reviewsquery += "(" + str(scores[i]) + ", \"" + str(year[i]) + "-" + str(month[i])+ "-" + str(day[i]) + "\", \"" + str(usernames[random.randint(0, len(usernames)-1)]) + "\", " + str(count) + "),\n"
            count += 1
    for j in americanFoods:
        for t in titles:
            query+= "(\""+j+"\", \"American\", \"" + t + j + "\", \"" + usernames[random.randint(0, len(usernames) - 1)]+"\"),\n"
            cnt_common = random.sample(range(0, 12), random.randint(1,6))
            cnt_s = random.sample(range(0, 9), random.randint(1,9))
            for c in cnt_common:
                ingredientOfquery += ("("+ str(count) + ", " + str(71 + c) + ", " + str(random.randint(1,10)) + ", \"" + str(measurements[random.randint(0,2)])+ "\"),\n")
            for c in cnt_s:
                ingredientOfquery += ("(" + str(count) + ", " + str(31 + c) + ", " + str(random.randint(1,10)) + ", \"" + str(measurements[random.randint(0,2)])+ "\"),\n")
            cnt_tools = random.sample(range(1,15), random.randint(1,14))
            for c in cnt_tools:
                toolsquery += ("(" + str(c) + ", " + str(count) + "),\n")
            cnt_restr = random.sample(range(1,10), random.randint(1,7))
            for c in cnt_restr:
                if c < 6:
                    restrquery += ("(" + str(count) + ", " + str(c) + "),\n")
            scores = [random.randint(1,5) for i in range (30)]
            year = [random.randint(2005, 2020) for i in range(30)]
            month = [random.randint(1, 12) for i in range(30)]
            day = [random.randint(1, 28) for i in range(30)]
            for i in range(30):
                reviewsquery += "(" + str(scores[i]) + ", \"" + str(year[i]) + "-" + str(month[i])+ "-" + str(day[i]) + "\", \"" + str(usernames[random.randint(0, len(usernames)-1)]) + "\", " + str(count) + "),\n"
            count += 1
    for j in indianFoods:
        for t in titles:
            query+= "(\""+j+"\", \"Indian\", \"" + t + j + "\", \"" + usernames[random.randint(0, len(usernames) - 1)] + "\"),\n"
            cnt_common = random.sample(range(0, 12), random.randint(1,6))
            cnt_s = random.sample(range(0, 9), random.randint(1,9))
            for c in cnt_common:
                ingredientOfquery += ("("+ str(count) + ", " + str(71 + c) + ", " + str(random.randint(1,10)) + ", \"" + str(measurements[random.randint(0,2)])+ "\"),\n")
            for c in cnt_s:
                ingredientOfquery += ("(" + str(count) + ", " + str(41 + c) + ", " + str(random.randint(1,10)) + ", \"" + str(measurements[random.randint(0,2)])+ "\"),\n")
            cnt_tools = random.sample(range(1,15), random.randint(1,14))
            for c in cnt_tools:
                toolsquery += ("(" + str(c) + ", " + str(count) + "),\n")
            cnt_restr = random.sample(range(1,10), random.randint(1,7))
            for c in cnt_restr:
                if c < 6:
                    restrquery += ("(" + str(count) + ", " + str(c) + "),\n")
            scores = [random.randint(1,5) for i in range (30)]
            year = [random.randint(2005, 2020) for i in range(30)]
            month = [random.randint(1, 12) for i in range(30)]
            day = [random.randint(1, 28) for i in range(30)]
            for i in range(30):
                reviewsquery += "(" + str(scores[i]) + ", \"" + str(year[i]) + "-" + str(month[i])+ "-" + str(day[i]) + "\", \"" + str(usernames[random.randint(0, len(usernames)-1)]) + "\", " + str(count) + "),\n"
            count += 1
    for j in vietnameseFoods:
        for t in titles:
            query+= "(\""+j+"\", \"Vietnamese\", \"" + t + j + "\", \"" + usernames[random.randint(0, len(usernames) - 1)]+ "\"),\n"
            cnt_common = random.sample(range(0, 12), random.randint(1,6))
            cnt_s = random.sample(range(0, 9), random.randint(1,9))
            for c in cnt_common:
                ingredientOfquery += ("("+ str(count) + ", " + str(71 + c) + ", " + str(random.randint(1,10)) + ", \"" + str(measurements[random.randint(0,2)])+ "\"),\n")
            for c in cnt_s:
                ingredientOfquery += ("(" + str(count) + ", " + str(51 + c) + ", " + str(random.randint(1,10)) + ", \"" + str(measurements[random.randint(0,2)])+ "\"),\n")
            cnt_tools = random.sample(range(1,15), random.randint(1,14))
            for c in cnt_tools:
                toolsquery += ("(" + str(c) + ", " + str(count) + "),\n")
            cnt_restr = random.sample(range(1,10), random.randint(1,7))
            for c in cnt_restr:
                if c < 6:
                    restrquery += ("(" + str(count) + ", " + str(c) + "),\n")
            scores = [random.randint(1,5) for i in range (30)]
            year = [random.randint(2005, 2020) for i in range(30)]
            month = [random.randint(1, 12) for i in range(30)]
            day = [random.randint(1, 28) for i in range(30)]
            for i in range(30):
                reviewsquery += "(" + str(scores[i]) + ", \"" + str(year[i]) + "-" + str(month[i])+ "-" + str(day[i]) + "\", \"" + str(usernames[random.randint(0, len(usernames)-1)]) + "\", " + str(count) + "),\n"
            count += 1
    for j in mexicanFoods:
        for t in titles:
            query+= "(\""+j+"\", \"Mexican\", \"" + t + j + "\", \"" + usernames[random.randint(0, len(usernames) - 1)] + "\"),\n"
            cnt_common = random.sample(range(0, 12), random.randint(1,6))
            cnt_s = random.sample(range(0, 9), random.randint(1,9))
            for c in cnt_common:
                ingredientOfquery += ("("+ str(count) + ", " + str(71 + c) + ", " + str(random.randint(1,10)) + ", \"" + str(measurements[random.randint(0,2)])+ "\"),\n")
            for c in cnt_s:
                ingredientOfquery += ("(" + str(count) + ", " + str(61 + c) + ", " + str(random.randint(1,10)) + ", \"" + str(measurements[random.randint(0,2)])+ "\"),\n")
            cnt_tools = random.sample(range(1,15), random.randint(1,14))
            for c in cnt_tools:
                toolsquery += ("(" + str(c) + ", " + str(count) + "),\n")
            cnt_restr = random.sample(range(1,10), random.randint(1,7))
            for c in cnt_restr:
                if c < 6:
                    restrquery += ("(" + str(count) + ", " + str(c) + "),\n")
            scores = [random.randint(1,5) for i in range (30)]
            year = [random.randint(2005, 2020) for i in range(30)]
            month = [random.randint(1, 12) for i in range(30)]
            day = [random.randint(1, 28) for i in range(30)]
            for i in range(30):
                reviewsquery += "(" + str(scores[i]) + ", \"" + str(year[i]) + "-" + str(month[i])+ "-" + str(day[i]) + "\", \"" + str(usernames[random.randint(0, len(usernames)-1)]) + "\", " + str(count) + "),\n"
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

    count = count -1

    mealquery = "INSERT INTO Meal(meal_name, description, username) \nValues"
    #for i in range(1,500):


    '''
    for i in range(amount):
        query += "\t("

        # employee ID
        query += str(i+1) + ", "

        # salary
        query += str(random.randint(12000, 150000)) + ", "

        # title
        possibleTitles = ["administrator", "engineer", "manager", "salesperson"]
        query += '"' + possibleTitles[random.randint(0,3)] + '"'

        if(i != amount-1):
            query += "),\n"
        else:
            query += ");"
    '''



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
