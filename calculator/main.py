from art import logo

print(logo)

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {"+" : add, "-": subtract, "*": multiply, "/": divide}

num1 = int(input("What's the first number? "))

for symbol in operations:
  print(symbol)

operation_symbol = input("Pick an operation from the line above ")

num2 = int(input("What's the second number? "))

answer1 = operations[operation_symbol](num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer1}")

operation_symbol = input("Pick another operation ")

num3 = int(input("What's the next number? "))

answer2 = operations[operation_symbol](answer1, num3)

print(f"{answer1} {operation_symbol} {num3} = {answer2}")
