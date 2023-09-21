number_one = 5
number_two = 7

if number_one > 3:
    print(number_one + number_two)
else:
    print("No se cumple")

number_two = "7"

try:
    print(number_one + number_two)
    print("Sin errores")
except:
    print("Con errores")


number_two = "10"

try:
    print(number_one + number_two)
    print("Sin errores")
except:
    print("Con errores")
else:
    print("La ejecucion continua")
finally:
    print("La ejecucion continua final")


number_two = "7"

try:
    print(number_one + number_two)
    print("Sin errores")
except TypeError as error:
    print(error)
except ValueError:
    print("Value Error")