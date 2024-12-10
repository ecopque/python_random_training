x = [1, 1, 4, 3, 8, 5, 7, 7, 0]
x = set(x)
print(x)
# Response: {0, 1, 3, 4, 5, 7, 8}

y = {1, 1, 2, 4, 7, 6, 5, 5, 0}
print(y)
# Response: {0, 1, 2, 4, 5, 6, 7}

u = x.union(y)
print(u)
# Response: {0, 1, 2, 3, 4, 5, 6, 7, 8}

v = x.intersection(y)
print(v)
# Response: {0, 1, 4, 5, 7}

w = x.difference(y)
print(w)
# Response: {8, 3}

a = x.symmetric_difference(y)
print(a)
# Response: {2, 3, 6, 8}

# Edson Copque | https://linktr.ee/edsoncopque
