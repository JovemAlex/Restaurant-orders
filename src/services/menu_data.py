# import pandas as pd
import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes: set[Dish] = set()
        self.load_menu_data(source_path)

    def load_menu_data(self, source_path: str) -> None:
        with open(source_path) as restaurant_file_csv:
            read_restaurant_file_csv = csv.DictReader(restaurant_file_csv)
            existing_dishes = {}

            for line in read_restaurant_file_csv:
                dish_name = line["dish"]
                price = float(line["price"])
                ingredient = Ingredient(line["ingredient"])
                amount = int(line["recipe_amount"])

                dish = Dish(dish_name, price)
                if repr(dish) not in existing_dishes:
                    existing_dishes[repr(dish)] = dish

                existing_dishes[repr(dish)].add_ingredient_dependency(
                    ingredient, amount
                )

            self.dishes = set(existing_dishes.values())
