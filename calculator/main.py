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

answer = 0

def compute(value1, value2, operation_symbol): 
  answer = operations[operation_symbol](value1, value2)

  print(f"{value1} {operation_symbol} {value2} = {answer}")

  return answer


num1 = int(input("What's the first number? "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation: ")

num2 = int(input("What's the next number? "))

answer = compute(num1, num2, operation_symbol)

keep_computing = True

while keep_computing:
  keepComputingPreference = input("Type 'y' to continue calculating, or type 'n' to exit.: \n")

  if keepComputingPreference == 'n':

    keep_computing = False

    exit()
  else:
    operation_symbol = input("Pick an operation ")

    num2 = int(input("What's the next number? "))

    answer = compute(answer, num2, operation_symbol)
