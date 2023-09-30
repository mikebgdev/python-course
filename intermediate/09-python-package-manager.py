import numpy
# import pandas
import requests
from mypackage import arithmetics

print(numpy.version.version)

numpy_array = numpy.array([34, 38, 66, 17, 19])
print(type(numpy_array))

print(numpy_array * 2)


response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())


print(arithmetics.sum_two_values(1, 4))