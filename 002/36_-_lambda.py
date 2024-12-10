import os
x = lambda: os.system('clear') # function
x()
# Response: clear (on terminal)

y = lambda: os.system('ls')
y()
# Response: ls

a = lambda: 10
print(a())
# Response: 10

b = lambda name, age: print(f'name={name} age={age}')
b('Edson', '100')
# Response: name=Edson age=100

c = lambda name, age: print(f'name={name}, age={age}')
c(name='Théo', age=50)
# Respose: name=Théo, age=50

d = lambda *args: print(f'args={args}')
d(1, 2, 3)
# Response: args=(1, 2, 3)

e = lambda **kwargs: print(f'kwargs={kwargs}')
e(a=1, b=2, c=3)
# Response: kwargs={'a': 1, 'b': 2, 'c': 3}

def my_function(*args, **kwargs):
    return (f'args={args}, kwargs={kwargs}')
f = my_function(name='Edson', age=150, height=173)
print(f)
# Response: args=(), kwargs={'name': 'Edson', 'age': 150, 'height': 173}

def my_new_function():
    return lambda *args: print(args)
g = my_new_function()
g(100)
# Response: (100,)

# Edson Copque | https://linktr.ee/edsoncopque
