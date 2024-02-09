with open('dishes.txt', 'r') as f:
    cook_book = f.read().split('\n\n')

def my_cook_book():
    ook_book = {}

    for string in cook_book:
        dish, _, *args = string.split('\n')
        dish_ingredients = []

        for arg in args:
            ingredient, quantity, measure = arg.split(' | ')
            dish_ingredients.append({'ingredient_name': ingredient, 'quantity': quantity, 'measure': measure})

            ook_book[dish] = dish_ingredients

    return ook_book
print(my_cook_book())

