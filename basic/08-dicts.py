my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Name": "Mike", "Surname": "Ballester", "Age": 29}

my_dict = {
    "Name": "Mike",
    "Surname": "Ballester",
    "Age": 29,
    "Languages": {"Python", "Php", "Java"}
}

print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Name"])

my_dict["Calle"] = "MikeDev"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Surname" in my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

my_list = ["name", 1, "age"]
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)