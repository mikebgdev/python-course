my_string = "My string"
my_other_strting = "My other string"

print(len(my_string))
print(len(my_other_strting))

print(my_string + " " + my_other_strting)

my_new_string = "Este es un string\ncon salto de linea"
print(my_new_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\\Este es un string \\n escapado"
print(my_scape_string)

name, surname, age = "Mike", "Ballester", 29
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")


#chars
language = "pyThon"
a, b, c, d, e, f = language
print(a)
print(e)

laguage_slice = language[1:3]
print(laguage_slice)

laguage_slice = language[1:]
print(laguage_slice)

laguage_slice = language[-2]
print(laguage_slice)

laguage_slice = language[::-1]
print(laguage_slice)

laguage_slice = language[0:6:2]
print(laguage_slice)


print(language.capitalize())
print(language.upper())
print(language.count("h"))
print(language.lower())
print(language.isnumeric())
print("1".isnumeric())
print(language.upper().count("T"))
print(language.istitle())