import json

with open("pokemons.json", "r") as read_file:
    data = json.load(read_file)

# access type
print(data['2'])
for item in data:
    print(data[item]["type"])
