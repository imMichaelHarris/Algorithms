#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # Both recipe and ingredients are dictionaries
  # Both will have the same foem 
  # Recipe is amount needed to complete
  # Ingredients is amount we have
  # Return the amount of batches we can make with the given ingredients
  # print("recipe", recipe.items())

  #
  batches = 0
  print(recipe.items())
  can_make = True
  while can_make == True:
    can_make = True
    for ingredient in recipe.items():
      # print("in", ingredient[0], "recipe", recipe[ingredient[0]])
      # print(ingredients)
      # print("ingred", ingredient[0], ingredients[ingredient[0]])
      print(hasattr(ingredients, ingredient[0]))
      print("ingredients", ingredients,ingredients[ingredient[0]], ingredient[0])
      if hasattr(ingredients, ingredient[0]) and ingredients[ingredient[0]] >= recipe[ingredient[0]]:
        print("yes", ingredients[ingredient[0]], recipe[ingredient[0]])
        ingredients[ingredient[0]] =  ingredients[ingredient[0]] - recipe[ingredient[0]]
      else:
        print("No more")
        can_make = False
        return batches
        print("Im here")
    batches += 1
    # for myingredient in ingredients.items():
    #   print(myingredient)


# recipe_batches({ 'milk': 100, 'butter': 50, 'flour': 5 }, { 'milk': 138, 'butter': 48, 'flour': 51 })
{ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 198, 'butter': 52, 'cheese': 10 }

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'cheese': 10 }
  ingredients = { 'milk': 198, 'butter': 52, 'cheese': 10 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))