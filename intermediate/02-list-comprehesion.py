my_original_list = [29, 30, 67, 90, 55, 17, 30]

my_list = [i for i in my_original_list]
print(my_list)

my_list = v
print(my_list)

my_list = [i + 2 for i in range(10)]
print(my_list)

my_list = [i * i for i in range(10)]
print(my_list)


def sum_five(number):
    return number + 5


my_list = [sum_five(i) for i in range(10)]
print(my_list)
