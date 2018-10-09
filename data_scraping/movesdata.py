import json

html = ""


import requests
from bs4 import BeautifulSoup

url = "https://bulbapedia.bulbagarden.net/wiki/List_of_moves"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

movesdata = {}

rows = soup.find(id="mw-content-text").select("table.sortable")[0].select("table.sortable")[0].select("tr")
for tr in rows:
    # cehck the generation cell
    generation = ""
    if tr.select("td:nth-of-type(9)"):
        generation = tr.select("td:nth-of-type(9)")[0].get_text()

    # only proceed in
    if len(generation) == 2 and "I" in generation[:1]:
        movenum = 0
        if tr.select("td:nth-of-type(1)"):
            movenum = int(tr.select("td:nth-of-type(1)")[0].get_text())


        movename = ""
        if tr.select("td:nth-of-type(2)"):
            movename = tr.select("td:nth-of-type(2)")[0].select("a")[0].get_text()

        movetype = ""
        if tr.select("td:nth-of-type(3)"):
            movetype = tr.select("td:nth-of-type(3)")[0].select("span")[0].get_text()

        movecategory = ""
        if tr.select("td:nth-of-type(4)"):
            movecategory = tr.select("td:nth-of-type(4)")[0].select("span")[0].get_text()

        movepp = 0
        if tr.select("td:nth-of-type(6)"):
            movepp = tr.select("td:nth-of-type(6)")[0].get_text()[:2]
            if "*" in movepp:
                movepp = movepp[:1]

        moveaccuracy = 0
        if tr.select("td:nth-of-type(8)"):
            moveaccuracy = tr.select("td:nth-of-type(8)")[0].get_text()
            indexOfPerc = 0
            try:
                indexOfPerc = moveaccuracy.index("%")
            except ValueError:
                moveaccuracy = None

            if indexOfPerc:
                moveaccuracy = int(moveaccuracy[:indexOfPerc])


        movesdata[movenum] = {}
        movesdata[movenum]["name"] = movename
        movesdata[movenum]["type"] = movetype
        movesdata[movenum]["category"] = movecategory
        movesdata[movenum]["pp"] = movepp
        movesdata[movenum]["accuracy"] = moveaccuracy


with open("moves.json", "w") as write_file:
    json.dump(movesdata, write_file)
