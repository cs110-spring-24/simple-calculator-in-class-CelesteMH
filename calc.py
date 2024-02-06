num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
operator = input("Enter your operator: ")

if operator == "+":
  print(f"{num1} + {num2} = {num1+num2}")
elif operator == "-":
  print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "/":
  if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
  else:
   print(f"{num1} / {num2} is undefined")
elif operator == "*":
  print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "**":
  print(f"{num1} ** {num2} = {num1 ** num2}")
elif operator == "//":
  print(f"{num1} // {num2} = {num1 // num2}")
elif operator == "%":
  print(f"{num1} % {num2} = {num1 % num2}")
else:
  print("try another valid operator: +, -, *, **, /, //, %")
