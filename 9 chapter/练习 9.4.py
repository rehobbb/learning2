class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type
        self.number_served=0
    def describe_restaurant(self):
        print(f"{self.restaurant_name}")
        print(f"{self.cuisine_type}")
    def set_number_served(self,number):
        self.number_served=number
    def number_restaurant(self):
        print(f"there are {self.number_served} people hanve been to the restaurant")
    def increment_number_served(self,number):
        self.number_served += number
restaurant=Restaurant("haoyunlai","zhongshi")
restaurant.set_number_served(25)
restaurant.number_restaurant()
restaurant.increment_number_served(5)
restaurant.number_restaurant()