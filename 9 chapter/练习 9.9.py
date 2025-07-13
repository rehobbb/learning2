class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model = model 
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it .")
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("you can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading += miles
class Battery:
    def __init__(self,battery_size=40):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"this car has a {self.battery_size} kWh battery.")
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range =225
        print(f"this car can go about {range} miles on a full charge.")
    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
class ElectriCar(Car):
    def __init__(self,make,model,year,size=40):
        super().__init__(make,model,year)
        self.battery = Battery(size)
my_leaf= ElectriCar('audi','a4',25)
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()