import json

class PokeData():
    def __len__(self):
        data = self.getData("pokemons.json")
        return len(data)

    def numByName(self, name):
        data = self.getData("pokemons.json")
        print(len(data))
        for item in data:
            if name.lower() == data[item]['name'].lower():
                return data[item]["dexnum"]

    def getTypes(self):
        data = self.getData("pokemons.json")
        types = []
        for item in data:
            for type in data[item]["type"]:
                if type not in types:
                    types.append(type)
        return types

    def getPokedex(self):
        data = self.getData("pokemons.json")

        return data

    def getPokedexOfType(self, type):
        data = self.getData("pokemons.json")
        data_of_type = {}
        for item in data:
            if type in data[item]['type'] :
                data_of_type[item]=data[item]
        return data_of_type

    def getEvolutionsOf(self, num):
        data = self.getData("pokemons.json")
        evolutions = {}
        for evolution in self.evolByNum(num):
            for item in data:
                if evolution in data[item]['name']:
                    evolutions[item] = data[item]
        return evolutions


    def getPokeByNum(self,num):
        data = self.getData("pokemons.json")
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


    def getData(self, filename):
        with open(filename, "r") as read_file:
            return json.load(read_file)

    def attributeByNum(self, attribute, num):
        data = self.getData("pokemons.json")
        return data[str(num)][attribute]
