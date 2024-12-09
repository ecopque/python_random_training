hd = []
while True:
    decision = int(input('Enter 1 to register and 2 to exit: '))
    if decision == 2:
        break
    else:
        name = str(input('Enter name: '))
        age = int(input('Enter age: '))
        height = float(input('Enter height: '))
        person = {'name': name, 'age': age, 'height': height}
        hd.append(person)
    print(hd)

# Edson Copque | https://linktr.ee/edsoncopque
