class Person:
    def __init__(self): # constructor method (__) | automatic
        print(f'Hello')

    def method_message(self):
        print('Method message.')

p1 = Person()
# Response: Hello

p1.method_message()
# Response: Method message

class NewPerson():
    def __init__(self, name, age, height):
        print(f'{name} | {age} | {height}')

p2 = NewPerson('Edson', 50, 70)
# Response: Edson | 50 | 70

# Edson Copque | https://linktr.ee/edsoncopque
