# Author: Gatlin Lawson

from product import Product

shopping_list = (
    Product("Hat", "Carolina snapback hat", 35.99),
    Product("Calculator", "Scientific Calulator", 21.99),
    Product("Controller", "Red Xbox controller", 49.99)
)

print("Your shopping List: ")
total_cost = 0
for product in shopping_list:
    product.display()
    total_cost += product.get_total_price()

print(f"Total cost: $ {round(total_cost, 2)}")