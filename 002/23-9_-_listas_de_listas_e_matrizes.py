nova_var = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, [3, 7, 9]],
]

print(nova_var[3][3][1])
print()

for i in range(0, len(nova_var)):
    for i2 in range(0, len(nova_var[i])):
        print(nova_var[i][i2])

  # Edson Copque | https://linktr.ee/edsoncopque
