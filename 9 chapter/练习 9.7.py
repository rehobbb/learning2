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
class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges =   ['can add post','can delet post','can ban user']
    def show_privileges(self):
        print("the permissions of the admin are:")
        for adm in self.privileges:
            print(f"{adm}")
admin_1 = Admin('tao','yang',23)           
admin_1.describe_user()
admin_1.show_privileges()

