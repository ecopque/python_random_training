class Person:
    def walk(self):
        print('Iam walking.')
    
    def speak(self):
        print('Iam speaking.')

class Customer(Person):
    def buy(self):
        print('Iam buying.')
    
    def speak(self): # see speak()/class Person
        super().speak() # 1o class Person (father) | 2o class Customer
        print('Haaaaaaa!')

c1 = Customer()
c1.speak() # Response: Iam speaking. | Haaaaaaa!
print()

################## 

class NewPerson:
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf

class NewCustomer(NewPerson):
    def __init__(self, id_customer, name, cpf):
        super().__init__(name, cpf) # class NewPerson with 'name' and 'cpf'
        self.id_customer = id_customer

c2 = NewCustomer(2, 'Edson', 888)
print(c2.id_customer) # Response: 2
print(c2.name) # Response: Edson

# Edson Copque | https://linktr.ee/edsoncopque
