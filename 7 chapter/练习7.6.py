
prompt = "\n how old are you?"

while True:
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("\n your ticket is free")
    elif age < 12:
        print("\n your ticket is 10 dollars")
    else:
        print("\n your ticket is 15 dollars")
    active = input("\n do you want to continue? (yes/no)")
    if active.lower() == 'no':
        break
    