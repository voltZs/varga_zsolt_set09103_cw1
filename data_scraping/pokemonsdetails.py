from bs4 import BeautifulSoup
import requests

url = "https://bulbapedia.bulbagarden.net/wiki/Squirtle"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# ALIAS
alias = ""
alias = soup.find(title="Pokémon category").select("span:nth-of-type(1)")[0]
if alias.select("span"):
    print(alias.select("span")[0].get_text())
else:
    print(alias.get_text())

# # DESCRIPTION
# description=""
# description = soup.find(id="Biology").parent.find_next_siblings("p")[0].get_text()
# print(description)


# HEIGHT

height=""
height = soup.find(id="mw-content-text").select("table:nth-of-type(22)")[0].select("tr")[0].select("td")[1].get_text()
print(int(float(height[:-2])*100))

# WEIGHT
height=""
height = soup.find(id="mw-content-text").select("table:nth-of-type(23)")[0].select("tr")[0].select("td")[1].get_text()
print(float(height[:-3]))

# CATCHRATE
catchrate=""
catchrate = soup.find(id="mw-content-text").select("table:nth-of-type(18)")[0].select("small")[0].previous_sibling
print(int(catchrate))


# HATCHTIME
hatchtime=""
hatchtime = soup.find(id="mw-content-text").select("table:nth-of-type(21)")[0].select("small")[0].previous_sibling
vals = hatchtime.split("-")
hatchtime_vals = []
for num in range(0, 2):
    hatchtime_vals.append(int(vals[num]))
print(hatchtime_vals)

# EVOLUTIONS
