class Die:
    def __init__(self,sides=6):
        self.sides = sides
    def roll_die(self):
        import random
        return random.randint(1,self.sides)
    
die1 = Die()
die2 = Die(10)
die3 = Die(20)
for i in range(10):
    print(f"6-sided die: {die1.roll_die()}")
    print(f"10-sided die: {die2.roll_die()}")
    print(f"20-sided die: {die3.roll_die()}")
    print("-" * 20)
print(range(10))