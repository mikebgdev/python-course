from functools import reduce


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_one(first_value, second_value, f_sum_one):
    return f_sum_one(first_value + second_value)


print(sum_two_values_and_one(4, 15, sum_one))
print(sum_two_values_and_one(4, 15, sum_five))


def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value

    return add


add_closure = sum_ten(1)
print(add_closure(5))

print(sum_ten(5)(4))

numbers = [2, 5, 10, 21, 3, 15]


def multiply_two(number):
    return number * 2


print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 3, numbers)))


def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False


print(list(filter(filter_greater_than_ten, numbers)))


def sum_two_values(first_value, second_value):
    return first_value + second_value


print(reduce(sum_two_values, numbers))
