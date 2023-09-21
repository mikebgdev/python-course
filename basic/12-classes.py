class MyEmptyPerson:
    pass


print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.name = name
        self.surname = surname
        self.full_name = f"{name} {surname} ({alias})"

    def walk(self):
        print(f"{self.full_name} esta caminando")


my_person = Person("Mike", "Ballester")

print(my_person.name)
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Mike", "Ballester", "MikeDev")
my_other_person.walk()
my_other_person.full_name = 'Miki Burn'

print(my_other_person.full_name)

my_other_person.full_name = 555

print(my_other_person.full_name)
