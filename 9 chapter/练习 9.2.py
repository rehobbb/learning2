class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type
    def describe_restaurant(self):
        print(f"{self.restaurant_name}")
        print(f"{self.cuisine_type}")
    def open_restaurant(self):
        print("the restaurant is opeing now")
restaurant1=Restaurant("xianglala","xiangcai")
restaurant2=Restaurant("feidachu","xiangcai")
restaurant3=Restaurant("baheli","chaoshancai")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()