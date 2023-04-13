recipe = {
    'ingredients' : [],
    'meal' : '',
    'prep_time' : 10,
}

cookbook = {
    'Sandwich' : {
        'ingredients' : ['ham', 'bread', 'cheese','tomatoes'],
        'meal' : 'lunch',
        'prep_time' : 10,
    },
    'Cake' : {
        'ingredients' : ['flour', 'sugar', 'eggs'],
        'meal' : 'dessert',
        'prep_time' : 60,
    },
    'Salad' : {
        'ingredients' : ['avocado','arugula','tomatoes','spinach'],
        'meal' : 'lunch',
        'prep_time' : 15,
    }
}
# A function that print all recipe names.
def printRecipeNames():
    print('Print the cookbook')
    for x in cookbook:
        print(x)

# A function that takes a recipe name and print its details.
def printRecipeDetails(recipeName):
    if recipeName in cookbook:
        print(f'\nRecipe for {recipeName}:')
        print(f"\tIngredients list: {cookbook[recipeName]['ingredients']}")
        print(f"\tTo be eaten for {cookbook[recipeName]['meal']}")
        print(f"\tTakes {cookbook[recipeName]['prep_time']} minutes of cooking")
    else:
        print(f'recipe : \'{recipeName}\' does not exist in the cookbook.')

def printRecipeDetailsHelper():
    print('\nPlease enter a recipe name to get its details:')
    printRecipeDetails(input('>> '))

# A function that takes a recipe name and deletes it
def deleteRecipe(recipeName):
    if recipeName in cookbook:
        cookbook.pop(recipeName)
    else:
        print(f'recipe : \'{recipeName}\' does not exist in the cookbook.')


def deleteRecipeHelper():
    print('\nPlease enter a recipe name to DELETE it:')
    deleteRecipe(input('>> '))

# A function that add a recipe from user input.
def addRecipe():
    print('Add a recipe')
    name = input('>>> Enter a name:\n')
    print('>>> Enter ingredients:')
    ingredients = []
    while (1):
        ingredient = input('')
        if ( ingredient == '' ): break
        ingredients.append(ingredient)
    meal = input('>>> Enter a meal type:\n')
    prep_time = input('>>> Enter a preparation time:\n')
    cookbook[name] = {'ingredients' : ingredients,'meal' : meal ,'prep_time' : prep_time}
    print(f'recipe \'{name}\' added successfully')

def quit():
    print('Cookbook closed. Goodbye !')
    exit()

# printRecipeNames()
# print('recipe details sandwich: \t')
# printRecipeDetails('Sandwich')
# # deleteRecipe(recipe)
# addRecipe()

def promptMenu():
    print('List of available option:')
    print('\t 1: Add a recipe')
    print('\t 2: Delete a recipe')
    print('\t 3: Print a recipe')
    print('\t 4: Print the cookbook')
    print('\t 5: Quit')



if __name__ == '__main__':
    actions = [addRecipe,deleteRecipeHelper,printRecipeDetailsHelper,printRecipeNames,quit]
    print('Welcome to the Python Cookbook !')
    promptMenu()
    while(1):
        print('\nPlease select an option: (1 - 5) OR --help')
        choice = input('>> ')
        if (choice == '--help'):
            promptMenu()
            continue
        if (choice.isnumeric() and int(choice) >= 1 and int(choice) <= 5):
                actions[int(choice) - 1]()
        else:
            print('Sorry, this option does not exist.')

# 1: Add a recipe
# 2: Delete a recipe
# 3: Print a recipe
# 4: Print the cookbook
# 5: Quit