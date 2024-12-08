x = [i for i in range(0, 10)]
print(x)
print()

y = []
for i in range(0, 10):
    y.append(i)
print(y)
print()

z = [i*2 for i in range(0, 10)]
print(z)
print()

a = [1, 2, 3, 4, 5]
b = [i*2 for i in a]
print(b)
print()

c = [input('Digite um nome: ') for i in range(0, 3)]
print(c)
print()

# d = [[j for j in range(0, 3)] for i in range(0, 5)]
# print(d)

d = [i for i in range(0, 10) if i > 7]
print(d)

# Edson Copque | https://linktr.ee/edsoncopque
