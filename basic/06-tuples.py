my_tuple = tuple()
my_other_tuple = ()

my_tuple =(29, 1.97, "Mike", "Ballester")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count(29))
print(my_tuple.index("Mike"))
print(my_tuple.index("Ballester"))


my_other_tuple = (30, 40, 50, 60, 70)
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[1:4])

my_tuple = list(my_tuple)
print(my_tuple)
print(type(my_tuple))