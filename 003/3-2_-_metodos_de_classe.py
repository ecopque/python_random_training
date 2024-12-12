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
        xxx = '888'
        return xxx

    def change_x(self, new_value):
        Person.x = new_value

    @classmethod
    def my_class_method(cls, parameter):
        cls.y = 999 # see class attribute 'y'
        print(f'New method: {parameter} and {cls.y}')

p1 = Person('Edson')
p1.my_class_method(55)
# Response: New method: 55

p2 = Person('John')
print(p2.y) # response: 999

Person.my_class_method(11) # wiwhout 'p1'
# Response: New method: 11 and 999

# Edson Copque | https://linktr.ee/edsoncopque
