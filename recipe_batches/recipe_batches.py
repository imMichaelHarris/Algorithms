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
  for ingredient in recipe.items():
    print("in", ingredient[0])
    print(ingredients)
    if ingredients[ingredient[0]] and :
      print("yes", ingredients[ingredient[0]])
  # for myingredient in ingredients.items():
  #   print(myingredient)

# recipe_batches({ 'milk': 100, 'butter': 50, 'flour': 5 }, { 'milk': 138, 'butter': 48, 'flour': 51 })

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))