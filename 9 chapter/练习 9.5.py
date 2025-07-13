class User:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.login_attemps=0
    def increment_login_attempts(self):
        self.login_attemps += 1
    def reset_login_attempts(self):
        self.login_attemps = 0
    def describe_user(self):
        print("\nthe personal resume is : ")
        print(f"{self.first_name}")
        print(f"{self.last_name}")
        print(f"{self.age}")
    def greet_user(self):
        print(f"hello my name is {self.first_name} {self.last_name},how are you?")
user1=User('liu','yi',23)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"you have login {user1.login_attemps} times!")
user1.reset_login_attempts()
print(f"you have login {user1.login_attemps} times!")
