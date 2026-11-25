import json
import os


class Animal:
    def __init__(self, species: str, name: str, sex: str = "Male" or "Female"):
        assert str(sex) in ("Male", "Female"), f"sex must be 'Male' or 'Female' not: {str(sex)}"
        animal = Animal.load_animal(species.lower())
        self.__id = id(animal)
        self.__species = animal["species"]
        self.name = str(name)
        self.__sex = str(sex)
        self.__decease = []

    @staticmethod
    def load_animal(animal):
        with open(os.sep.join(["data", "species.json"])) as species:
            species = species.read()
            if animal not in (json.loads(species).keys()):
                animal = 'dog'
            return json.loads(species)[animal]


if __name__ == '__main__':
    test_animal = Animal(name="Pablo", species="Dog", sex="Male")
    print(vars(test_animal))
    test_animal2 = Animal(name="Michelle", species="Cat", sex="Female")
    print(vars(test_animal2))
