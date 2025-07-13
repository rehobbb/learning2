class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type
    def describe_restaurant(self):
        print(f"{self.restaurant_name}")
        print(f"{self.cuisine_type}")
    def open_restaurant(self):
        print("the restaurant is opeing now")
class IceCreamStand(Restaurant):
    def __init__(self,name,type):
        super().__init__(name,type)
        self.flavors = ['sweet','chocolate','apple']
    def desplay_icecream(self):
        print(f"the flavors of the icecream are {self.flavors}")
icecream = IceCreamStand('mcdoload','good')
icecream.desplay_icecream()
