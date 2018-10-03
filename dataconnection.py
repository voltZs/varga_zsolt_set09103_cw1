import json

class PokeData():
    def __len__(self):
        with open("pokemons.json", "r") as read_file:
            data = json.load(read_file)
        return len(data)

    def numByName(self, name):
        with open("pokemons.json", "r") as read_file:
            data = json.load(read_file)
        for item in data:
            if name.lower() in data[item]['name'].lower():
                return data[item]["dexnum"]
    def getPokeByNum(self,num):
        with open("pokemons.json", "r") as read_file:
            data = json.load(read_file)
        return data[str(num)]

    def nameByNum(self, num):
        return self.attributeByNum("name", num)

    def aliasByNum(self, num):
        return self.attributeByNum("alias", num)

    def imgByNum(self, num):
        return self.attributeByNum("image", num)

    def sprByNum(self, name):
        return self.attributeByNum("sprite", num)

    def typeByNum(self, num):
        return self.attributeByNum("type", num)

    def descrByNum(self, num):
        return self.attributeByNum("description", num)

    def evolByNum(self, num):
        return self.attributeByNum("evolutions", num)

    def heightByNum(self, num):
        return self.attributeByNum("height", num)

    def weightByNum(self, num):
        return self.attributeByNum("weight", num)


    def attributeByNum(self, attribute, num):
        with open("pokemons.json", "r") as read_file:
            data = json.load(read_file)
        return data[str(num)][attribute]
