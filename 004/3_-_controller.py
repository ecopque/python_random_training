# Logic

from dal import PersonDal
from model import PersonModel

class PersonController:
    @classmethod
    def registercontroller(cls, name: str, age: int, cpf: int):
        if len(name) > 2 and (age > 0 and age < 200) and len(str(cpf)) == 11:
            try:
                PersonDal.savedal(PersonModel(name, age, cpf))
                return True
            except:
                return False

PersonController.registercontroller('Victor', 100, 12345678912)

# Edson Copque | https://linktr.ee/edsoncopque
