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
                if evolution == data[item]['name']:
                    evolutions[item] = data[item]
        return evolutions

    def getPokeByNum(self,num):
        data = self.getData("pokemons.json")
        return data[str(num)]

    def nameByNum(self, num):
        return self.attributeByNum("name", num)

    def evolByNum(self, num):
        return self.attributeByNum("evolutions", num)

    def attributeByNum(self, attribute, num):
        data = self.getData("pokemons.json")
        return data[str(num)][attribute]




    def getPokedexOfMove(self, move):
        dex = self.getPokedex();
        altered_dex = {}
        for pokemon in dex:
            if move in dex[pokemon]['moves']:
                altered_dex[pokemon]= dex[pokemon]
        return altered_dex

    def getMove(self, move):
        moves = self.getData("moves.json")
        for index in moves:
            if moves[index]['name'] == move:
                return moves[index]

        return None

    def getMoves(self):
        data = self.getData("moves.json")
        return data


    def getTypes(self):
        types = self.getData("poketypes.json")
        return types





    def getData(self, filename):
        with open(filename, "r") as read_file:
            return json.load(read_file)
