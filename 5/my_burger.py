def add_ingredient(ingredient):
    print(f"Adding {ingredient}")


def make_double_cheese_burger():
    ingredients = ["Bunn", "Mayo", "Meat", "Cheese", "Meat", "Cheese", "Pickles", "Tomatoes", "Mayonnaise", "Bunn"]

    for ingredient in ingredients:
        add_ingredient(ingredient)


make_double_cheese_burger()