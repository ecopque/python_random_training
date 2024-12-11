class XXX:
    def xxx(self):
        print('xxx.')

class Animal:
    def walk(self):
        print('Im walking like an animal.')
    
    def run(self):
        print('Im running.')

    def jump(self):
        print('Im jumping.')

class Feline(Animal):
    def nocturnal(self):
        print('Im act at night.')

class Cat(Feline):
    def meow(self):
        print('Miouuuu...')

class Dog(Animal, XXX):
    def barking(self):
        print('Au au.')

x = Cat()
x.meow() # Miouuuu...
x.nocturnal() # Im act at night.
x.jump() # Im jumping.

y = Dog()
y.run() # Im running.
y.xxx() # xxx.

# Edson Copque | https://linktr.ee/edsoncopque
