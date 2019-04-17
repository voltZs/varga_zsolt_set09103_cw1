import json
from dataconnection import PokeData

pokedata = PokeData()

print(pokedata.getTypes())

# with open("pokemons.json", "r") as read_file:
#     data = json.load(read_file)
#
# # access type
# print(data['2'])
# for item in data:
#     print(data[item]["type"])
