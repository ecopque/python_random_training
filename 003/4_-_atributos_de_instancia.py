class Person:
    def __init__(self, name):
        self.name = name

    def my_friend(self):
        return self.name
    
    def my_print(self):
        print(self.my_friend())

p1 = Person('Edson')
p1.my_print()

# Edson Copque | https://linktr.ee/edsoncopque
