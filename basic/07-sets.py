my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {29, "Mike", "Ballester"}
print(type(my_other_set))

print(len(my_other_set))

print(my_other_set)

my_other_set.add("Miki")
print(my_other_set)

my_other_set.add("Mike")
print(my_other_set)

print("Mike" in my_other_set)
print("Mike2" in my_other_set)

my_other_set.remove("Mike")
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

my_set = {29, "Mike", "Ballester"}
my_other_set = {"Python", "Dev"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)