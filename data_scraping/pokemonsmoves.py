import requests
from bs4 import BeautifulSoup

url = "https://bulbapedia.bulbagarden.net/wiki/Meowth_(Pok%C3%A9mon)/Generation_I_learnset"
response = requests.get(url)
moves = []
tempMoves = []
soup = BeautifulSoup(response.text, "html.parser")
for tr in soup.find(id="mw-content-text").select("table.sortable")[0].select("tr"):
    tempMoves.append(tr.select("span:nth-of-type(2)")[0].get_text())

for num in range(1, len(tempMoves)):
    moves.append(tempMoves[num])
tempMoves = []

for tr in soup.select("table:nth-of-type(5)")[0].select("tr"):
    if tr.select("span:nth-of-type(2)"):
        tempMoves.append(tr.select("span:nth-of-type(2)")[0].get_text())

for num in range(4, len(tempMoves)):
    moves.append(tempMoves[num])

print(moves)



# [0].get_text()


# with open("archive/"+pageNum+".txt", "w") as dest:
#     response = requests.get(url)
#     text = response.text
#     dest.write(text)
