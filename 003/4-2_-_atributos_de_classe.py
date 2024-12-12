class Person:
    x = 'Hello' # class attribute
    y = 123456

    def __init__(self, name):
        self.name = name

    def my_friend(self):
        return self.name
    
    def my_print(self):
        print(self.my_friend())

    def my_new_method(self):
        return '888'

    def change_x(self, new_value):
        Person.x = new_value

p1 = Person('Edson')
p1.name = 'Edsuuu'
p1.my_print()
# Response: Edsuuu

print(Person('Sagan').my_new_method())
# Response: 888

x2 = Person.x
print(x2)
# Response: Hello

Person.x = 'New value'
x3 = Person.x
print(x3)
# Response: New value

p2 = Person('Théo')
print(p2.x)
# Response: New value

p2.change_x('Hello change_x')
print(p2.x)
# Response: Hello change_x

# Edson Copque | https://linktr.ee/edsoncopque
