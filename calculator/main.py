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

def calculator():
  answer = 0

  def compute(value1): 
    operation_symbol = input("Pick an operation: ")

    value2 = float(input("What's the next number? "))

    answer = operations[operation_symbol](value1, value2)

    print(f"{value1} {operation_symbol} {value2} = {answer}")

    return answer


  num1 = float(input("What's the first number? "))

  for symbol in operations:
      print(symbol)

  answer = compute(num1)

  keep_computing = True

  while keep_computing:
    keep_computing_preference = input("Type 'y' to continue calculating, type 'r' to restart, type 'n' to exit: \n")

    if keep_computing_preference == 'r':
      keep_computing = False
      # Recursion
      calculator()
    elif keep_computing_preference == 'n':
      exit()
    else:
      answer = compute(answer)

calculator()
