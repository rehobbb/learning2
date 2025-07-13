class User:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def describe_user(self):
        print("\nthe personal resume is : ")
        print(f"{self.first_name}")
        print(f"{self.last_name}")
        print(f"{self.age}")
    def greet_user(self):
        print(f"hello my name is {self.first_name} {self.last_name},how are you?")
