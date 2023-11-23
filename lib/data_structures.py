spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

new_food = {
        "name": "Chapaii",
        "cuisine": "Kenyan",
        "heat_level": 6,
    }

def get_names(spicy_foods):
    return [food.get('name') for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get('heat_level') > 5]
  
def print_spicy_foods(spicy_foods):
    return [print(f"{food.get('name')} ({food.get('cuisine')}) | Heat Level: {'🌶' * food.get('heat_level')}") for food in spicy_foods]

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    found_food = [food for food in spicy_foods if food.get('cuisine') == cuisine]
    return found_food[0]

def print_spiciest_foods(spicy_foods):
    return [print(f"{food.get('name')} ({food.get('cuisine')}) | Heat Level: {'🌶' * food.get('heat_level')}") for food in spicy_foods if food.get('heat_level') > 5]

def get_average_heat_level(spicy_foods):
    heat_level_list = [food.get('heat_level') for food in spicy_foods]
    heat_level_total = sum(heat_level_list)
    return heat_level_total / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    