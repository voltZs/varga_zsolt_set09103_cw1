import requests
import json
from bs4 import BeautifulSoup

with open("moves.json", "r") as read_file:
    pokemoves = json.load(read_file)

pokemoves_alt = pokemoves

for move in pokemoves:

    url = "https://bulbapedia.bulbagarden.net/wiki/" + pokemoves[move]['name'] +"_(move)"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.find(id="Description").parent.find_next_siblings()[0].select("tr")
    tds = rows[len(rows)-1].select("td")
    info = tds[len(tds)-1].get_text()
    # typeinfostr = ""
    # for item in typeinfo:
    #     typeinfostr = typeinfostr + item
    print(pokemoves[move]['name'] + "--------------")
    print(info)

    pokemoves_alt[move]["description"] = info


with open("moves_updated.json", "w") as write_file:
    json.dump(pokemoves_alt, write_file)
