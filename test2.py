responses = {}
polling_active = True
while polling_active:
    name = input("\n what is your name?")
    response = input("which mountain would you like to climb someday?")
    responses[name]=response
    repeat = input("would you like to continue?")
    if repeat == "no":
        polling_active = False
print("\n......the polling result ........")
for name,response in responses.items():
    print(f"{name} like to climb the {response} mountain")