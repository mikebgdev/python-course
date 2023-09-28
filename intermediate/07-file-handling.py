import json
import csv

# TXT

txt_file = open("./files/my_file.txt", "w+")

txt_file.write(
    "Mi nombre es Mike\nMi apellido es Ballester\n29 años\nY mi lenguaje preferido es Python")

# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta Php")
print(txt_file.readline())

txt_file.close()

with open("./files/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY JavaScript")


# JSON

json_file = open("./files/my_file.json", "w+")

json_test = {
    "name": "Mike",
    "surname": "Ballester",
    "age": 29,
    "languages": ["Python", "Php"],
    "website": "https://mikebgdev.com"}

json.dump(json_test, json_file, indent=2)

json_file.close()

with open("./files/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("./files/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# CSV


csv_file = open("./files/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Mike", "Ballester", 29, "Python", "https://mikebgdev.com"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()
