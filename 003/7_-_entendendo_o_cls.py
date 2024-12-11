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

    @classmethod #1: | decorator
    def my_class_method(cls):
        cls.x = 2 # modifies class attribute 'x' directly
        return None


print(Person.x) # class attribute
# Response: Hello

Person.my_class_method() # ???
print(Person.x)
# Response: 2

#1: The first parameter is cls, which refers to the class itself, not a specific instance. This allows you to access or modify class attributes and methods (attributes shared by all instances of the class).

# Edson Copque | https://linktr.ee/edsoncopque
