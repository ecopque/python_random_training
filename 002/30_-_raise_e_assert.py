def my_sum(n1, n2):
    if n1 < 0 or n2 < 0:
        raise ValueError('n1 or n2 can not be negative.')
    else:
        return n1 + n2

print(my_sum(1, -2))

x = -1
assert x > 0, 'Problem.'

# Edson Copque | https://linktr.ee/edsoncopque
