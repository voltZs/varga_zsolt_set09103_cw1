import requests
import json
from bs4 import BeautifulSoup

pokevolutions = {}

url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_evolution_family"
response = requests.get(url)




soup = BeautifulSoup(response.text, "html.parser")
rows = soup.find(id="mw-content-text").select("table")[0].select("tr")

temp_evol1 = ""
tuple_evol = []
matrix_evolutions = []
for tr in rows:

    if tr.select("td"):
        evol1 = ""
        evol2 = ""
        evol3 = ""

        if tr.select("td")[1].select("span"):
            evol1 = tr.select("td")[1].select("span")[0].get_text()
            temp_evol1 = evol1
        else:
            evol1 = temp_evol1
        tuple_evol.append(evol1)

        if len(tr.select("td")) == 4:
            evol2 = tr.select("td")[2].select("span")[0].get_text()
        elif len(tr.select("td")) >= 4:
            evol2 = tr.select("td")[4].select("span")[0].get_text()
        if evol2:
            tuple_evol.append(evol2)


        if len(tr.select("td")) >= 7:
            evol3 = tr.select("td")[7].select("span")[0].get_text()
        if evol3:
            tuple_evol.append(evol3)

        matrix_evolutions.append(tuple_evol)
        tuple_evol = []

# print(matrix_evolutions)

for i in range(0, len(matrix_evolutions)):
    for j in range(0, len(matrix_evolutions[i])):
        pokevolutions[matrix_evolutions[i][j]] = []

for pokemon in pokevolutions:
    for i in range(0, len(matrix_evolutions)):
        for j in range(0, len(matrix_evolutions[i])):
            for k in range(0, len(matrix_evolutions[i])):
                if matrix_evolutions[i][k] not in pokevolutions[matrix_evolutions[i][j]]:
                    pokevolutions[matrix_evolutions[i][j]].append(matrix_evolutions[i][k])

# print(pokevolutions)

with open("pokemonevolutions.json", "w") as write_file:
    json.dump(pokevolutions, write_file)
