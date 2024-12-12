# Database access | persistent storage

from model import PersonModel

class PersonDal:
    @classmethod
    def savedal(cls, person: PersonModel):
        with open('persons.txt', 'w') as file:
            file.write(person.name + ' ' + str(person.age) + ' ' + str(person.cpf))
    
    @classmethod
    def readtal(cls):
        name = 'Edson'
        age = 100
        cpf = 123456
        return PersonModel(name, age, cpf)

# Creating a Personodel instance:
p1 = PersonModel('Edsuu', 50, 987654321)

# Saving data to file:
PersonDal.savedal(p1)

# Reading data:
print(PersonDal.readtal().cpf)

# Edson Copque | https://linktr.ee/edsoncopque
