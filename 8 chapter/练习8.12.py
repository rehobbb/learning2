def sanwich(sandwich_type,*toppings):
    print(f"\nmaking a {sandwich_type} sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
sanwich('san1','tomato')
sanwich('san2','lectture','egg')
sanwich('san3','egg','pork','beef')
