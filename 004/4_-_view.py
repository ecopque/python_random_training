# Graphical interface

from controller import PersonController
from dal import PersonDal

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

    elif decision == 2:
        try:
            read = PersonDal.readdal()
            print(f'Name: {read.name}, Age: {read.age}, CPF: {read.cpf}')
        except FileNotFoundError:
            print('No person has been registered yet.')
        except Exception as error_var:
            print(f'An error occurred: {error_var}.')
          

# Edson Copque | https://linktr.ee/edsoncopque
