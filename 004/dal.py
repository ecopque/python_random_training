# Database access | persistent storage

from model import PersonModel

class PersonDal:
    @classmethod
    def savedal(cls, person: PersonModel):
        with open('persons.txt', 'w') as file:
            file.write(person.name + ' ' + str(person.age) + ' ' + str(person.cpf))
    
    @classmethod
    def readdal(cls):
        # name = 'Edson'
        # age = 100
        # cpf = 123456
        with open('persons.txt', 'r') as file:
            data = file.read().split()
            name = data[0]
            age = int(data[1])
            cpf = int(data[2])
        return PersonModel(name, age, cpf)

# Creating a PersonModel instance:
p1 = PersonModel('Edsuu', 50, 987654321)

# Saving data to file:
PersonDal.savedal(p1)

# Reading data:
print(PersonDal.readdal().cpf)

# Edson Copque | https://linktr.ee/edsoncopque
