from users import User
class Privileges:
    def __init__(self):
        self.pri = ['can add post','can delet post','can ban user']
    def show_privileges(self):
        print("the permissions of the admin are:")
        for adm in self.pri:
            print(f"{adm}")
class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.priv1 = Privileges()