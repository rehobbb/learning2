print("input two numbers , i will return the sum of the two numbers")
a = input("please input the first number:")
b = input("please input the seconde number")
try:
  sum = int(a)+int(b)
  print(f"the sum of the two numbers is {sum}")
except ValueError:
  print("please input the value not the string!")