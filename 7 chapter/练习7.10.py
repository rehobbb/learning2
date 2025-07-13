holidays={}
activate=True
while activate:
    name = input("what's your name? ")
    place = input("if you could visit one place in the world, where would it be? ")
    holidays[name] = place
    cont = input("do you want to continue? (yes/no)")
    if cont.lower() != 'yes':
        activate = False
for name,place in holidays.items():
    print(f"{name} would like to visit {place}.")