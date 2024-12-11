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

    @classmethod
    def my_class_method(cls, parameter):
        print(f'New method: {parameter}')

p1 = Person('Edson')
p1.my_class_method(55)
# Response: New method: 55

Person.my_class_method(11)
# Response: New method: 11

# Edson Copque | https://linktr.ee/edsoncopque
