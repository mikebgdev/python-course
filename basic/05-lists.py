my_list = list()
my_other_list = []

print(len(my_list))
print(len(my_other_list))

my_list = [29, 30, 67, 90, 55, 17, 30]

print(my_list)
print(len(my_list))

my_other_list = [29, 1.97, "Mike", "Ballester"]

print(type(my_other_list))

print(my_other_list[-1])
print(my_other_list[0])
print(my_other_list[-3])
print(my_other_list[3])
print(my_other_list.count(29))

age, height, name, surname = my_other_list

print(name)

print(my_list + my_other_list)

my_other_list.append("Dev")
print(my_other_list)

my_other_list.insert(1, "Python")
print(my_other_list)

my_other_list.remove("Python")
print(my_other_list)

my_list.remove(30)
print(my_list)

my_list.pop()
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()
print(my_new_list)

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])