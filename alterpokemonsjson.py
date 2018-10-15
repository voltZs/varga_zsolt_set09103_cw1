import json

with open("pokemons.json", "r") as read_file:
    pokemons = json.load(read_file)

new_dex = []

for pokemon in range(1,152):
    poke_obj = {}
    pokemon = str(pokemon)
    poke_obj["dexnum"] = pokemons[pokemon]["dexnum"]
    poke_obj["name"] = pokemons[pokemon]["name"]
    poke_obj["type"] = pokemons[pokemon]["type"]
    poke_obj["alias"] = pokemons[pokemon]["alias"]
    poke_obj["description"] = pokemons[pokemon]["description"]
    poke_obj["moves"] = pokemons[pokemon]["moves"]
    poke_obj["evolutions"] = pokemons[pokemon]["evolutions"]
    poke_obj["height"] = pokemons[pokemon]["height"]
    poke_obj["weight"] = pokemons[pokemon]["weight"]
    poke_obj["catchrate"] = pokemons[pokemon]["catchrate"]
    poke_obj["hatchtime"] = pokemons[pokemon]["hatchtime"]
    new_dex.append(poke_obj)

with open("pokemons_updated.json", "w") as write_file:
    json.dump(new_dex, write_file)
