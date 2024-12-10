# lambda <parameters>: <expression>

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
y = list(filter(lambda parameter: parameter <= 10 and parameter % 2==0, x))
print(y)
# Response: [2, 4, 6, 8, 10]

###
def is_less_than_10(parameter):
    return parameter <= 10 and parameter % 2==0

result_hd = []
for i in x:
    if is_less_than_10(i):
        result_hd.append(i)
print(result_hd)
# Response: [2, 4, 6, 8, 10]

###
b = [{'name': 'Edson', 'age': 15}, {'name': 'Carl', 'age': 100}]
a = list(filter(lambda parameter: parameter['age'] >= 50, b))
print(a)
# Response: [{'name': 'Carl', 'age': 100}]

# Edson Copque | https://linktr.ee/edsoncopque
