bonus = [3,45,2,6,7,8,9,10,11,12,13,14,15,'da','er','san','si','wu']
reward = [45,10,'da','san']
import random
def get_bonus():
    return random.choice(bonus)
def get_bonus_list(n):
    bonus_list = []
    for i in range(n):
        bonus_list.append(get_bonus())
    return bonus_list
i = 0
while True:
    bonus1 = get_bonus_list(4)
    if bonus1 == reward:
        print(f"the bonus list is: {bonus1}")
        break
    else:
        i += 1
print(f"there are {i} times to get the bonus list! ")
