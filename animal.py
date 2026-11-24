import json


def species_json(animal):
    with open("species.json") as species:
        if species not in (json.loads(species.read()).keys()):
            species = "dog"
        return json.loads(species.read())[animal]


class Animal:
    def __init__(self, species: str, name: str, sex: str = "Male" or "Female"):
        assert str(sex) in ("Male", "Female"), f"sex must be 'Male' or 'Female' not: {str(sex)}"
        animal = species_json(species.lower())
        self.__id = id(animal)
        self.__species = animal["species"]
        self.name = str(name)
        self.__sex = str(sex)
        self.__decease = []


if __name__ == '__main__':
    test_animal = Animal(name="Pablo", species="Dog", sex="Male")
    print(vars(test_animal))
    test_animal2 = Animal(name="Michelle", species="Cat", sex="Female")
    print(vars(test_animal2))
