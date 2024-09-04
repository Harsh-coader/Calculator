# calculator

first = int(input("Enter your first number : "))
second = input("Operator : +, -, %, /, * ")
third = int(input("Enter your second number : "))

if second == "+":
  print(first + third)

elif second == "-":
  print(first - third)

elif second == "*":
  print(first * third)

elif second == "%":
  print(first % third)

elif second == "/":
  print(first / third)

else:
  print("ERROR")
