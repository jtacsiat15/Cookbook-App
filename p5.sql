-- 1) search query
-- selects all recipe_id, recipe name, user's name, avg(review)
-- 
-- 2) queries to get recipe details:

-- 2.1) select step number and desciption of all instructions corresponding to a
-- specific recipe_id

-- 2.2) select ingredient name, amount, and measurement unit, recipe_id for each ingredient used
-- in a specific recipe

-- 2.3) select restriction name that correspond to recipe_id

-- 2.4) select cooking tool names that correspond to recipe_id

-- 2.5) select cuisine type, food type, avg rating, user's name

-- 3) query for list of meals
-- select name of meal for specific username (current user)

-- 4) query to get more info on meals

-- 4.1) select meal name, description, user's name given a meal_id

-- 4.2) select all recipes corresponding to specific meal

-- 5) query for list of recipes
-- select name of recipe for specific username

-- 6) query to get contents of recipe - same as 2)


-----------------------------------------
-- possible other queries

-- top 5 ingredients used in some specified cuisine type

-- search for recipes with a rating number that is at least some number

-- search for meal that includes certain recipes

-- search for meals where average rating of recipes in meal is above a certain number

-- search for users where the average rating of the recipes they make is above a certain
-- number and the number of recipes they made is above a certain number.

-- select all meals that include some number of recipes that specifify some specific dietary
-- restriction
