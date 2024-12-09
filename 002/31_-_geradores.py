# pip install pympler
from pympler.asizeof import asizesof

#####

# NORMAL FUNCTION
def function_double(my_list):
    double_list = []
    for i in my_list:
        double_list.append(i*2)
    return double_list

x = function_double(range(0, 100))
print(x)

y = asizesof(x)
print(y)
print()

#####

# GENERATING FUNCTION
def double():
    yield 1
    yield 2
    yield 3

x = double()
print(next(x))
print(next(x))
print(next(x))
print()

#####
def function_generate(parameter):
    for i in parameter:
        yield i * 2
z = function_generate(range(0, 1000))
print(next(z))
print(next(z))
print(asizesof(z)) # Response: (592,).

def function_generate2(parameter):
    my_list = []
    for i in parameter:
        my_list.append(i * 2)
    return my_list
w = function_generate2(range(0, 1000))
print(asizesof(w)) # Response: (40856,).

# Edson Copque | https://linktr.ee/edsoncopque
