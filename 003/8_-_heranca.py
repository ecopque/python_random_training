class Person:
    def walk(self):
        print('I can walk.')
    def speak(self):
        print('I can talk.')

class Customer(Person):
    def buy(self):
        print('I can buy.')

class Seller(Person):
    def seller(self):
        print('I can sell.')

c1 = Customer()
c1.speak() # I can talk.
c1.buy() # I can buy.

s1 = Seller()
s1.walk() # I can walk.
s1.seller() # I can sell.

# Edson Copque | https://linktr.ee/edsoncopque
