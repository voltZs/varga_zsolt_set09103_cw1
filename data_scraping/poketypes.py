import requests
import json
from bs4 import BeautifulSoup
types = ["Grass", "Poison", "Fire", "Flying", "Water", "Bug", "Normal", "Electric", "Ground", "Fairy", "Fighting", "Psychic", "Rock", "Steel", "Ice", "Ghost", "Dragon"]


poketypes = {}

for type in types:

    url = "https://bulbapedia.bulbagarden.net/wiki/"+ type +"_(type)"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    typeinfo = soup.find(id="mw-content-text").select("p")[0].find_all(text=True)

    typeinfostr = ""
    for item in typeinfo:
        typeinfostr = typeinfostr + item
    print(type)
    print(typeinfostr)

    poketypes[type] = {}
    poketypes[type]['description'] = typeinfostr


with open("poketypes.json", "w") as write_file:
    json.dump(poketypes, write_file)
