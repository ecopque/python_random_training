x = [i for i in range(1, 25)]
a = list(map(lambda parameter: 1 if parameter < 18 else(parameter), x))
print(x)
# Response: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
print(a)
# Response: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 18, 19, 20, 21, 22, 23, 24]


c = [{'name': 'Edson', 'age': 25}, {'name': 'Suyama', 'age': 60}]
d = list(map(lambda value: {'name': value['name'], 'age': -1} if value['age'] < 30 else(value), c))
print(d)
# Response: [{'name': 'Edson', 'age': -1}, {'name': 'Suyama', 'age': 60}]

# Edson Copque | https://linktr.ee/edsoncopque
