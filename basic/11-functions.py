def my_function():
    print("Esto es una funcion")


my_function()
my_function()
my_function()


def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)


sum_two_values(5, 7)
sum_two_values(54754, 72272)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)


def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value


my_result = sum_two_values_with_return(10, 5)
print(my_result)


def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Ballester", name="Mike")


def print_name_with_default(name="Miki", surname="Ball"):
    print(f"{name} {surname}")


print_name_with_default()


def print_texts(*text):
    print(text)


print_texts('Hola', 'Python', 'Mike')
