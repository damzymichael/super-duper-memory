MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {"water": 300, "milk": 200,  "coffee": 100}
"""
1 Penny -> 1 cent -> $0.01
1 Dime -> 10 cents -> $0.1
1 Nickel -> 5 cents -> $0.05
1 Quarter -> 25 cents -> $0.25
"""
class Coffee_Machine:
  is_active = False
  profit = 0
  def __init__(self, menu=MENU, resources=resources):
    self.menu = menu
    self.resources = resources
    self.is_active = True

  def print_report(self):
    for key, value in self.resources.items():
      print(f"{key.title()}: {value}{"g" if key == "coffee" else "ml"}")
    print(f"Money: ${self.profit}")

  def is_resources_sufficient(self, user_choice):
    for key in self.menu[user_choice]["ingredients"].keys():
      if self.resources[key] - self.menu[user_choice]["ingredients"][key] < 0:
        print(f"Not enough {key} for this order.\nOrder again")
        return False
    return True

  def collect_user_input(self):
    is_invalid_input = True
    total = 0
    while is_invalid_input:
      try:
        total += round(int(input("How many quarters?: ")) * 0.25, 2)
        total += round(int(input("How many dimes?: ")) * 0.1, 2)
        total += round(int(input("How many nickles?: ")) * 0.05, 2)
        total += round(int(input("How many pennies?: ")) * 0.01, 2)
        is_invalid_input = False
        return total
      except:
        invalid_user_input = True
        print("Invalid cost input, Re-enter inputs")

  def is_cost_covered(self, user_choice, total):
    change = total - self.menu[user_choice]["cost"]
    if change < -1:
      print("Cost higher than entered amount")
      return False
    elif change > 0:
      print(f"Here is {change} in change ")
    return True

  def update_resources(self, user_choice, total):
    ingredients = self.menu[user_choice]["ingredients"]
    for key in ingredients:
      self.resources[key] = self.resources[key] - ingredients[key]
    self.profit += self.menu[user_choice]["cost"]

  def show_success_message(self, user_choice):
    print(f"Here is your {user_choice.title()} ☕ Enjoy!")