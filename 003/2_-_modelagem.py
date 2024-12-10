class Person:
    def __init__(self, name, age, cpf):
        self.name = name
        self.age = age
        self.cpf = cpf

    def login_system(self):
        print(f'{self.name}: Logging into the system.')

p1 = Person('Edson Copque', 50, 99988877755)
p2 = Person('Johny Winter', 150, 11122233344)

print(p1.name)
# Response: Edson Copque

print(p1.login_system())
# Response: Edson Copque: Logging into the system.

# Edson Copque | https://linktr.ee/edsoncopque
