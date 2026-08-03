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

profit = 0

resources = {"water": 300, "milk": 200,  "coffee": 100}

"""
1 Penny -> 1 cent -> $0.01
1 Dime -> 10 cents -> $0.1
1 Nickel -> 5 cents -> $0.05
1 Quarter -> 25 cents -> $0.25
"""
conversion = {"pennies": 0.01, "dimes": 0.1, "nickles": 0.05, "quarters": 0.25}

'''
1 penny = $0.01
'''

is_coffee_machine_active = True

while is_coffee_machine_active:
    user_choice = input("What would you like? (espresso, latte, cappuccino)\nYou can also type report to see our resources: ").strip()

    if user_choice not in MENU.keys() and user_choice != "report":
        print("Invalid command")
    elif user_choice == "report":
        for key, value in resources.items():
            print(f"{key.title()}: {value}{"g" if key == "coffee" else "ml"}")
        print(f"Money: ${profit}")
    else:
        # Check if there's enough resources for what the user wants before asking for money
        ingredients = MENU[user_choice]["ingredients"]
        found_incomplete_resources = False
        for key in ingredients.keys():
            if resources[key] - ingredients[key] < 0:
                print("Not enough resources for this order.\nOrder again")
                found_incomplete_resources = True
                continue
        if found_incomplete_resources:
            continue
        
        print("Please insert coins")
        invalid_user_input = True
        user_money_input = {"quarters": 0, "dimes": 0, "nickles": 0, "pennies": 0}
        while invalid_user_input:
            try:
                user_money_input["quarters"] = int(input("How many quarters?: "))
                user_money_input["dimes"] = int(input("How many dimes?: "))
                user_money_input["nickles"] = int(input("How many nickles?: "))
                user_money_input["pennies"] = int(input("How many pennies?: "))
                invalid_user_input = False
            # When this is not specified, the system sees keyboard interrupt as an error
            except ValueError:
                invalid_user_input = True
                print("Invalid cost input, Re-enter inputs")
        total_in_dollar = 0
        for key,value in user_money_input.items():
            total_in_dollar += round(conversion[key] * value, 2)
        change = total_in_dollar - MENU[user_choice]["cost"]
        # Check if money is enough
        if change < 0:
            print("Cost exceeds entered price")
            continue
        
        # Subtract needed resources from current resources
        for key in ingredients.keys():
            resources[key] = resources[key] - ingredients[key]

        # Add total to profit
        profit += MENU[user_choice]["cost"]

        if change > 0:
            # If successful
            # print change if there's change
            print(f"Here is {round(change, 2)} in change")
        
        # print success message to user
        print(f"Here is your {user_choice.title()} ☕ Enjoy!")
