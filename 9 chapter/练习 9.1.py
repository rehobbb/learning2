class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type
    def describe_restaurant(self):
        print(f"{self.restaurant_name}")
        print(f"{self.cuisine_type}")
    def open_restaurant(self):
        print("the restaurant is opeing now")
restaurant=Restaurant("haoyunlai","zhongshi")
print(f"{restaurant.restaurant_name} is a {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()