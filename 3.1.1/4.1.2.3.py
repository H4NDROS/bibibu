class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age
pet = Pet()
name = input("Введите имя питомца: ")
pet.set_name(name)
animal_type = input("Введите тип питомца: ")
pet.set_animal_type(animal_type)
age = input("Введите возраст питомца: ")
pet.set_age(age)
print("Имя питомца:", pet.get_name())
print("Тип питомца:", pet.get_animal_type())
print("Возраст питомца:", pet.get_age())