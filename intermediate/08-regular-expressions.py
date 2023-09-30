import re

my_string = "Leccion: leccion Expresiones Regulares"
my_other_string = "No es la leccion: Ficheros"

print(re.match("Leccion", my_string))
print(re.match("Leccion", my_other_string))
print(re.match("Leccion", my_string, re.I).span())
start, end = re.match("Leccion", my_string, re.I).span()
print(re.match("Leccion", my_string, re.I).start())
print(re.match("Leccion", my_string, re.I).end())

print(my_string[start:end])


print(re.search("regulares", my_string, re.I))

print(re.findall("regulares", my_string, re.I))

print(re.split(":", my_string, re.I))

print(re.sub(":","-->",my_string))
print(re.sub("[l|L]eccion","LECCION",my_string))


pattern = r"[lL]eccion"
print(re.findall(pattern,my_string, re.I))

pattern = r"[0-9]"
print(re.findall(pattern,my_string, re.I))

pattern = r"\D"
print(re.findall(pattern,my_string, re.I))

pattern = r"[l].*"
print(re.findall(pattern,my_string, re.I))


email = "mike@mikebgdev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "mike@mikebgdev.com.es"
print(re.findall(pattern, email))


