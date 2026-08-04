from coffe_machine import Coffee_Machine

coffee_machine = Coffee_Machine()

while coffee_machine.is_active:
  user_choice = input("What would you like? (espresso, latte, cappuccino)\nYou can also type report to see our resources\nOr enter 'off' to turn of the machine: ").strip()
  if user_choice == "off":
    coffee_machine.is_active = False
  elif user_choice == "report":
    coffee_machine.print_report()
  elif user_choice not in coffee_machine.menu.keys():
    print("Invalid command")
  else:
    if not coffee_machine.is_resources_sufficient(user_choice):
      continue
    is_invalid_input = True
    total = coffee_machine.collect_user_input()
    if not coffee_machine.is_cost_covered(user_choice, total):
      continue
    coffee_machine.update_resources(user_choice, total)
    coffee_machine.show_success_message(user_choice)
