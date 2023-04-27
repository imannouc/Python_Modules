

class Recipe:
    def __init__(self,name,cooking_lvl,cooking_time,ingredients,description,recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_time = recipe_type
        assert isinstance(name, str)
        assert isinstance(cooking_lvl, int)
        assert isinstance(cooking_time, int)
        assert isinstance(ingredients, list)
        assert isinstance(description, str)
        assert isinstance(recipe_type, str)
        assert cooking_lvl in range(1,6)
        assert cooking_time > 0
        assert recipe_type in ["starter", "lunch", "dessert"]
    
    def __str__():
        """Return the string to print with the recipe info"""
        txt = ""
        return txt