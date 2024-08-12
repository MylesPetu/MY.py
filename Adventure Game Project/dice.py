import random


class Dice:
    def __init__(self):
        pass
        # self.roll()
        # self.wroll()


    def roll(self):
        x = random.randint(1, 6)
        print(f"You rolled a {x}")
        return x
    def wroll(self):
        x = random.randint(1, 6)
        print(f"Madam Koi Koi rolled a {x}")
        return x
