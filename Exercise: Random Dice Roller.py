import random

random.randint(1,6)

def dice_roller(side, num):
    for i in range (num):
        print(random.randint(1, side))  


dice_roller(6, 7)

