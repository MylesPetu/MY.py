"""
class PizzaOrder:
    def __init__(self, size, add_pepperoni, extra_cheese):
        self.size = size
        self.add_pepperoni = add_pepperoni
        self.extra_cheese = extra_cheese
        self.size_price = self.get_size_price()
        self.final_price = self.calculate_final_price()

    def get_size_price(self):
        if self.size == 's':
            return 15
        elif self.size == 'm':
            return 20
        elif self.size == 'l':
            return 25
        else:
            raise ValueError("Invalid pizza size")

    def calculate_final_price(self):
        price = self.size_price

        if self.add_pepperoni:
            if self.size == 's':
                price += 1
            else:
                price += 2

        if self.extra_cheese:
            price += 1

        return price

    def get_order_summary(self):
        return (f"Order Summary: \n"
                f"Pizza Size: {self.size} Pizza\n "
                f"Add Pepperoni: {'y' if self.add_pepperoni else 'n'}\n"
                f"Extra Cheese: {'y' if self.extra_cheese else 'n'}\n"
                f"Final Price: ${self.final_price}")


# Example usage
def main():

    size = input("What size of pizza would you like to have (s, m, l): ").upper()
    add_pepperoni = input("Do you want pepperoni? (y or n): ").upper() == 'y'
    extra_cheese = input("Do you want extra cheese? (y or n): ").upper() == 'y'

    order = PizzaOrder(size, add_pepperoni, extra_cheese)
    print(order.get_order_summary())


if __name__ == "__main__":
    main()
"""

def fizzbuzz(n):
    n = 100
    for i in range(1, n+1):
        print(fizzbuzz_value(i))


def fizzbuzz_value(i):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(str(i))


fizzbuzz(101)
