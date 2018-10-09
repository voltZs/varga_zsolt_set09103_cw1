import requests
import time
import json
from bs4 import BeautifulSoup

url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"

response = requests.get(url)

moves = []
tempMoves = []

with open("pokemonevolutions.json", "r") as read_file:
    evolutions_dict = json.load(read_file)

soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find(id="mw-content-text").select("table:nth-of-type(2)")[0].select("tr")

pokemons = {}
for tr in rows:
    dexnum = ""
    if tr.select("td:nth-of-type(1)"):
        dexnum = tr.select("td:nth-of-type(1)")[0].get_text()[2:]

    # only do anything with the row if the dexnum contains a number
    if "1" in dexnum or "0" in dexnum:
        dexnum = int(dexnum)

        pokename = ""
        if tr.select("td:nth-of-type(4)"):
            pokename = tr.select("td:nth-of-type(4)")[0].select("a:nth-of-type(1)")[0].get_text()

        type = []
        if tr.select("td:nth-of-type(5)"):
            type.append(tr.select("td:nth-of-type(5)")[0].select("span:nth-of-type(1)")[0].get_text())
        if tr.select("td:nth-of-type(6)"):
            type.append(tr.select("td:nth-of-type(6)")[0].select("span:nth-of-type(1)")[0].get_text())

        print(pokename)

        # MAKE REQUEST FOR MOVES OR A POKEMON
        # url = "https://bulbapedia.bulbagarden.net/wiki/"+pokename+"_(Pok%C3%A9mon)/Generation_I_learnset"
        # response = requests.get(url)
        # moves = []
        # tempMoves = []
        # soup = BeautifulSoup(response.text, "html.parser")
        # for tr in soup.find(id="mw-content-text").select("table.sortable")[0].select("tr"):
        #     tempMoves.append(tr.select("span:nth-of-type(2)")[0].get_text())
        #
        # for num in range(1, len(tempMoves)):
        #     moves.append(tempMoves[num])
        # tempMoves = []
        #
        # for tr in soup.select("table:nth-of-type(5)")[0].select("tr"):
        #     if tr.select("span:nth-of-type(2)"):
        #         tempMoves.append(tr.select("span:nth-of-type(2)")[0].get_text())
        #
        # for num in range(4, len(tempMoves)):
        #     moves.append(tempMoves[num])
        # time.sleep(1)
        #
        # # MAKE REQUEST FOR  DETAILS OF A POKEMON
        # url = "https://bulbapedia.bulbagarden.net/wiki/" + pokename
        # response = requests.get(url)
        #
        # # ALIAS
        # alias = ""
        # soup = BeautifulSoup(response.text, "html.parser")
        #
        # alias = soup.find(title="Pokémon category").select("span:nth-of-type(1)")[0]
        # if alias.select("span"):
        #     alias = alias.select("span")[0].get_text()
        # else:
        #     alias = alias.get_text()
        #
        #
        # #DESCRIPTION
        # description=""
        # description = soup.find(id="Biology").parent.find_next_siblings("p")[0].get_text()
        #
        # # HEIGHT
        # height=""
        # height = soup.find(id="mw-content-text").select("table:nth-of-type(22)")[0].select("tr")[0].select("td")[1].get_text()
        # height = int(float(height[:-2])*100)
        #
        # # WEIGHT
        # weight=""
        # weight = soup.find(id="mw-content-text").select("table:nth-of-type(23)")[0].select("tr")[0].select("td")[1].get_text()
        # weight = float(weight[:-3])
        #
        # # CATCHRATE
        # catchrate=""
        # catchrate = soup.find(id="mw-content-text").select("table:nth-of-type(18)")[0].select("small")[0].previous_sibling
        # catchrate = int(catchrate)
        #
        # # HATCHTIME
        # hatchtime=""
        # hatchtime = soup.find(id="mw-content-text").select("table:nth-of-type(21)")[0].select("small")[0].previous_sibling
        # vals = hatchtime.split("-")
        # hatchtime_vals = []
        # for num in range(0, 2):
        #     hatchtime_vals.append(int(vals[num]))
        #
        #
        # pokemons[dexnum] = {}
        # pokemons[dexnum]["dexnum"] = dexnum
        # pokemons[dexnum]["name"] = pokename
        # pokemons[dexnum]["sprite"] = str(dexnum)+".png"
        # pokemons[dexnum]["image"] = pokename.lower()+"_img.png"
        # pokemons[dexnum]["type"] = type
        # pokemons[dexnum]["alias"] = alias
        # pokemons[dexnum]["description"] = description
        #
        # # pokemons[dexnum]["moves"] = moves
        # pokemons[dexnum]["evolutions"] = evolutions_dict[pokename]
        # pokemons[dexnum]["height"] = height
        # pokemons[dexnum]["weight"] = weight
        # pokemons[dexnum]["catchrate"] = catchrate
        # pokemons[dexnum]["hatchtime"] = hatchtime_vals
        #
        # print(pokemons[dexnum])
        # # time.sleep(1)


# with open("pokemons1.json", "w") as write_file:
#     json.dump(pokemons, write_file)





# "dexnum" : 1,
# "name" : "Bulbasaur",
# "sprite" : "1.png",
# "image" : "bulbasaur_img.png",
# "type" : ["Grass", "Poison"],

# "alias" : "Seed Pokémon",
# "description" : "Bulbasaur is a small, quadruped Pokémon that has blue-green skin with darker green patches. It has red eyes with white pupils and scleras. It also has pointed, ear-like structures on top of its head. Its snout is short and blunt, and it has a wide mouth. A pair of small, pointed teeth are visible in the upper jaw when its mouth is open. Each of its thick legs ends with three sharp claws. On its back is a green plant bulb, which is grown from a seed planted there at birth. The bulb provides it with energy through photosynthesis as well as from the nutrient-rich seeds contained within.",
# "moves" : ["Tackle", "Growl", "Leech Seed", "Vine Whip", "PoisonPowder", "Razor Leaf", "Growth", "Sleep Powder", "SolarBeam", "Swords Dance", "Toxic", "Body Slam", "Take Down", "Double-Edge", "Rage", "Mega Drain", "Mimic", "Double Team", "Reflect", "Bide", "Rest", "Substitute", "Cut"],
# "evolutions" : ["Bulbasaur", "Ivysaur", "Venosaur"],
# "height" : 70,
# "weight" : 6.9,
# "catchrate" : ,
# "hatchtime" :
