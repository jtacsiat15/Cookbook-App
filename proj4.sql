/*----------------------------------------------------------------------
 * Name: Anna Smith and Jalen Tacsiat
 * File: proj4.sql
 * Date: 10/22/2020
 * Class: CPSC 321 - Databases
 * Description: Create and insert statements for our recipes database
 ----------------------------------------------------------------------*/

-- required in MariaDB to enforce constraints
SET sql_mode = STRICT_ALL_TABLES;

DROP TABLE IF EXISTS RecipesInMeals;
DROP TABLE IF EXISTS RecipeHasDietaryRestrictions;
DROP TABLE IF EXISTS CookingToolsRequired;
DROP TABLE IF EXISTS IngredientOf;
DROP TABLE IF EXISTS Instruction;
DROP TABLE IF EXISTS Ingredient;
DROP TABLE IF EXISTS Rating;
DROP TABLE IF EXISTS Recipe;
DROP TABLE IF EXISTS Meal;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS CookingTool;
DROP TABLE IF EXISTS DietaryRestriction;

CREATE TABLE DietaryRestriction(
  restriction_id INT UNSIGNED AUTO_INCREMENT,
  restriction_name VARCHAR(50) UNIQUE NOT NULL,
  PRIMARY KEY (restriction_id)
);

CREATE TABLE CookingTool(
  tool_id INT UNSIGNED AUTO_INCREMENT,
  tool_name VARCHAR(50) UNIQUE NOT NULL,
  PRIMARY KEY (tool_id)
);

CREATE TABLE User(
  username VARCHAR(50) CHECK (LENGTHB(password) >= 5),
  name VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL CHECK (LENGTHB(password) >= 8),
  PRIMARY KEY (username)
);

CREATE TABLE Meal(
  meal_id INT UNSIGNED AUTO_INCREMENT,
  meal_name VARCHAR(50) NOT NULL,
  description VARCHAR(100),
  username VARCHAR(50),
  PRIMARY KEY (meal_id),
  FOREIGN KEY (username) REFERENCES User(username) ON DELETE SET NULL
);

CREATE TABLE Recipe(
  recipe_id INT UNSIGNED AUTO_INCREMENT,
  food_type VARCHAR(30),
  cuisine_type VARCHAR(30),
  recipe_title VARCHAR(30) NOT NULL,
  username VARCHAR(50),
  PRIMARY KEY (recipe_id),
  FOREIGN KEY (username) REFERENCES User(username) ON DELETE SET NULL
);

CREATE TABLE Rating(
  rating_id INT UNSIGNED AUTO_INCREMENT,
  score SMALLINT UNSIGNED NOT NULL CHECK (score <= 5),
  date_added DATE,
  username VARCHAR(50),
  recipe_id INT UNSIGNED NOT NULL,
  PRIMARY KEY (rating_id),
  FOREIGN KEY (username) REFERENCES User(username) ON DELETE SET NULL,
  FOREIGN KEY (recipe_id) REFERENCES Recipe(recipe_id) ON DELETE CASCADE
);

CREATE TABLE Ingredient(
  ingredient_id INT UNSIGNED AUTO_INCREMENT,
  ingredient_name VARCHAR(30) UNIQUE NOT NULL,
  recipe_id INT UNSIGNED,
  PRIMARY KEY (ingredient_id),
  FOREIGN KEY (recipe_id) REFERENCES Recipe(recipe_id) ON DELETE SET NULL
);

CREATE TABLE Instruction(
  recipe_id INT UNSIGNED,
  step_number SMALLINT UNSIGNED,
  description VARCHAR(800) NOT NULL,
  PRIMARY KEY (recipe_id, step_number),
  FOREIGN KEY (recipe_id) REFERENCES Recipe(recipe_id) ON DELETE CASCADE
);

CREATE TABLE IngredientOf(
  recipe_id INT UNSIGNED,
  ingredient_id INT UNSIGNED,
  amount DECIMAL(5, 2) UNSIGNED NOT NULL,
  measurement_units VARCHAR(20),
  PRIMARY KEY (recipe_id, ingredient_id),
  FOREIGN KEY (ingredient_id) REFERENCES Ingredient(ingredient_id) ON DELETE CASCADE,
  FOREIGN KEY (recipe_id) REFERENCES Recipe(recipe_id) ON DELETE CASCADE
);

CREATE TABLE CookingToolsRequired(
  tool_id INT UNSIGNED,
  recipe_id INT UNSIGNED,
  PRIMARY KEY (recipe_id, tool_id),
  FOREIGN KEY (tool_id) REFERENCES CookingTool(tool_id) ON DELETE CASCADE,
  FOREIGN KEY (recipe_id) REFERENCES Recipe(recipe_id) ON DELETE CASCADE
);

CREATE TABLE RecipeHasDietaryRestrictions(
  recipe_id INT UNSIGNED,
  restriction_id INT UNSIGNED,
  PRIMARY KEY (recipe_id, restriction_id),
  FOREIGN KEY (restriction_id) REFERENCES DietaryRestriction(restriction_id) ON DELETE CASCADE,
  FOREIGN KEY (recipe_id) REFERENCES Recipe(recipe_id) ON DELETE CASCADE
);

CREATE TABLE RecipesInMeals(
  recipe_id INT UNSIGNED,
  meal_id INT UNSIGNED,
  PRIMARY KEY (recipe_id, meal_id),
  FOREIGN KEY (meal_id) REFERENCES Meal(meal_id) ON DELETE CASCADE,
  FOREIGN KEY (recipe_id) REFERENCES Recipe(recipe_id) ON DELETE CASCADE
);

INSERT INTO DietaryRestriction (restriction_name)
  VALUES ("Vegan"),
          ("Vegetarian"),
          ("Lactose intolerant"),
          ("gluten free");

INSERT INTO CookingTool (tool_name)
  VALUES ("pot"),
          ("spatula"),
          ("oven"),
          ("stovetop"),
          ("grill"),
          ("blender");

INSERT INTO User (username, name, password)
  VALUES ("gordonramsay123", "Gordon Ramsay", "hellskitchen"),
          ("altonbrown_1", "Alton Brown", "iLik3toCook"),
          ("guyfieri420", "Guy Fieri", "triple_D!"),
          ("spongebob2", "Spongebob Squarepants", "krustykrab");

INSERT INTO Recipe (food_type, cuisine_type, recipe_title, username)
  VALUES ("pizza", "italian", "Pizza Margherita on Focaccia", "gordonramsay123"),
          ("Bread", "italian", "Focaccia Bread", "gordonramsay123"),
          ("Pizza", "Italian", "Pepperoni Pizza", "guyfieri420"),
          ("Burger", "America", "Cheeseburger", "spongebob2"),
          ("Soup", "Japanese", "Miso Soup", "altonbrown_1");

INSERT INTO Ingredient (ingredient_name, recipe_id)
  VALUES ("Focaccia Bread", NULL),
          ("Marinara Sauce", NULL),
          ("Cheese", NULL),
          ("Tomatoes", NULL),
          ("Basil", NULL),
          ("Balsamic Glaze", NULL),
          ("Flour", NULL),
          ("Salt", NULL),
          ("Yeast", NULL),
          ("Water", NULL),
          ("Olive Oil", NULL),
          ("Vegetable Broth", NULL),
          ("Nori", NULL),
          ("Leeks", NULL),
          ("Scallions", NULL),
          ("Tofu", NULL),
          ("Miso", NULL),
          ("Pepperoni", NULL),
          ("Dough", NULL),
          ("Burger meat", NULL),
          ("Buns", NULL),
          ("Condiments", NULL),
          ("Lettuce", NULL);

INSERT INTO Rating (score, date_added, username, recipe_id)
  VALUES (5, '2015-04-03', "gordonramsay123", 4),
          (1, '2019-02-05', "gordonramsay123", 3),
          (4, '2017-06-12', "altonbrown_1", 2),
          (3, '2018-07-11', "guyfieri420", 2),
          (5, '2019-01-10', "spongebob2", 5),
          (5, '2020-01-04', "spongebob2", 1);

INSERT INTO IngredientOf (recipe_id, ingredient_id, amount, measurement_units)
  VALUES (2, 7, 3.25, "cups"),
          (2, 8, 1, "tablespoon"),
          (2, 9, .5, "teaspoons"),
          (2, 10, 1.75, "cups"),
          (2, 11, 4, "tablespoons");

INSERT INTO IngredientOf (recipe_id, ingredient_id, amount, measurement_units)
  VALUES (1, 1, 1, NULL),
          (1, 2, .25, "cups"),
          (1, 3, 6, "oz"),
          (1, 4, 1, "cup"),
          (1, 5, 1, "oz"),
          (1, 6, 2, "tablespoons");

INSERT INTO IngredientOf(recipe_id, ingredient_id, amount, measurement_units)
  VALUES (3, 2, 5, "cups"),
          (3, 3, 3, "oz"),
          (3, 18, 20, "slices");

INSERT INTO IngredientOf(recipe_id, ingredient_id, amount, measurement_units)
  VALUES (4, 22, 5, "cups"),
          (4, 20, 3, "oz"),
          (4, 3, 2, "slices");

INSERT INTO IngredientOf(recipe_id, ingredient_id, amount, measurement_units)
  VALUES (5, 12, 6, "cups"),
          (5, 13, 1, "sheet"),
          (5, 14, 1, NULL),
          (5, 15, 3, NULL),
          (5, 16, 8, "oz"),
          (5, 17, 2, "tablespoons");

INSERT INTO Instruction (recipe_id, step_number, description)
  VALUES (2, 1, "Whisk together the flour, kosher salt and yeast. Add the warm water to the flour mixture and stir until incorporated."),
          (2, 2, "Pour 2 tablespoons oil into a medium bowl. Transfer the dough to the bowl, cover with plastic wrap."),
          (2, 3, "Place in the refrigerator to rest for 24 hours."),
          (2, 4, "Brush the inside of a 9-by-13-inch baking sheet with oil. Remove the dough from the refrigerator and transfer to the prepared pan."),
          (2, 5, "Using your hands, spread the dough out as much as possible, adding oil to the dough if needed to keep it from sticking."),
          (2, 6, "Place the dough in a warm place and let rise until about doubled in size. Then, spread out on sheet."),
          (2, 7, "Heat the oven to 450 degrees. Pat down the focaccia to an even thickness of about 1 inch."),
          (2, 8, "Drizzle it with the remaining 2 tablespoons olive oil. Sprinkle with salt."),
          (2, 9, "Bake, rotating once front to back, until the top is uniformly golden brown, 20 to 25 minutes. Cool for 20 minutes");

INSERT INTO Instruction (recipe_id, step_number, description)
  VALUES (1, 1, "Preheat oven to 375."),
          (1, 2, "Spread focaccia bread with pizza sauce, and top with mozzarella and tomatoes."),
          (1, 3, "Cook until cheese melts.  Broil for a minute or so until the cheese is just starting to char on the tops of bubbles."),
          (1, 4, "Top with basil and balsamic glaze.");

INSERT INTO Instruction(recipe_id, step_number, description)
  VALUES (3, 1, "Set up Buns"),
          (3, 2, "Put condiment here"),
          (3, 3, "Put burger on bun"),
          (3, 4, "Close bun");

INSERT INTO Instruction(recipe_id, step_number, description)
  VALUES (4, 1, "Set up Dough"),
          (4, 2, "Put sauce on dough"),
          (4, 3, "Put Pepperoni on dough"),
          (4, 4, "Put cheese on dough"),
          (4, 5, "Bake");

INSERT INTO Instruction(recipe_id, step_number, description)
  VALUES (5, 1, "Heat vegetable broth over medium heat until simmering."),
          (5, 2, "Add nori, leeks, scallions, and tofu. Let simmer 5 more minutes."),
          (5, 3, "In a small bowl, stir miso paste with just enough water to dilute."),
          (5, 4, "Add contents of bowl to broth and let simmer a minute or so more.");

INSERT INTO CookingToolsRequired(tool_id, recipe_id)
  VALUES (5, 4),
          (2, 4),
          (3, 3),
          (3, 2),
          (1, 5),
          (3, 1);

INSERT INTO RecipeHasDietaryRestrictions (recipe_id, restriction_id)
  VALUES(2, 2),
        (1, 2),
        (5, 1),
        (5, 2);

INSERT INTO Meal(meal_name, description, username)
  VALUES ("Burgers and pizza", "A burger and a pizza", "gordonramsay123"),
          ("Pizza and Soup", "A pizza and some Japanese Miso Soup", "guyfieri420"),
          ("Burgers with Focaccia Bread", "Burgers using Focaccia Bread", "spongebob2");

INSERT INTO RecipesInMeals (recipe_id, meal_id)
  VALUES (3, 1),
          (4, 1),
          (1, 2),
          (5, 2),
          (4, 3),
          (2, 3);

SELECT *
FROM DietaryRestriction;

SELECT *
FROM CookingTool;

SELECT *
FROM Recipe;

SELECT *
FROM User;

SELECT *
FROM Ingredient;

SELECT *
FROM Rating;

SELECT *
FROM IngredientOf;

SELECT *
FROM Instruction;

SELECT *
FROM CookingToolsRequired;

SELECT *
FROM Meal;
