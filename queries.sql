SELECT DISTINCT m.meal_name, m.meal_id, COUNT(*)
FROM Meal m JOIN RecipesInMeals rm ON (m.meal_id = rm.meal_id)
GROUP BY m.meal_id
HAVING COUNT(*) >= 1 AND COUNT(*) <= 3;
