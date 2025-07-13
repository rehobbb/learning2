print("input two numbers , \n" 
"i will return the sum of the two numbers")
print('if you want to quit,please input "q"')
while True:
  a = input("please input the first number:")
  if a == 'q':
    break
  b = input("please input the seconde number:")
  try:
    sum = int(a)+int(b)
    print(f"the sum of the two numbers is {sum}")
  except ValueError:
    print("please input the value not the string!")
    continue