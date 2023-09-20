my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print("Mi condicion es mayor o igual a 10")

print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es 15")
        break

    print("Es menor que 20")

print("List")
my_list = [35, 40, 60, 70, 93, 22, 11, 29]

for element in my_list:
    print(element)

print("Tuple")
my_tuple = (29, 1.97, "Mike", "Ballester")

for element in my_tuple:
    print(element)

print("Set")
my_set = {29, "Mike", "Ballester"}

for element in my_set:
    print(element)

print("Dict")
my_dict = {"Name": "Mike", "Surname": "Ballester", "Age": 29}

for element in my_dict:
    print(element)
    if element == "Age":
        break

print("Dict values")

for element in list(my_dict.values()):
    print(element)
else:
    print("fin bucle")