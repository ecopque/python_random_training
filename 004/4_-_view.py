# Graphical interface

from controller import PersonController

while True:
    decision = int(input('Enter 1 to register, 2 to see the saved person or 3 to exit: '))
    if decision == 3:
        break

    elif decision == 1:
        name = str(input('Enter your name: '))
        age = int(input('Enter your age: '))
        cpf = int(input('Enter your cpf: '))

        if PersonController.registercontroller(name, age, cpf):
            print('User registered successfully!')
        else:
            print('Enter valid values.')
          

# Edson Copque | https://linktr.ee/edsoncopque
