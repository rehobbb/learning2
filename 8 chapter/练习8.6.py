def city_country(name, country):
    response = f"{name.title()}, {country.title()}"
    return response
while True:
    print("\n enter 'q' at any time to quit.")
    name = input("enter a city name:")
    if name.lower() == 'q':
            break
    country = input('enter a country name:')
    if country.lower() == 'q':
            break
    print(city_country(name, country))