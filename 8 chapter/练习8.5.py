def describe_city1(name,country='china'):
    print(f"{name.title()} is in {country.title()}.")
describe_city1('beijing')
describe_city1('paris','farance')
describe_city1(name='shanghai')