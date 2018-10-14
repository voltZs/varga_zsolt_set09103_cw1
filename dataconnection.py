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

    def getFilteredPokedex(self, dex_filter):
        dex = self.getPokedex()
        filtered_dex = {}
        for dexnum in dex:
            pokemon = dex[dexnum]
            if self.passesDexFilter(pokemon, dex_filter):
                filtered_dex[dexnum] = dex[dexnum]
        return filtered_dex

    def passesDexFilter(self, pokemon_obj, dex_filter):
        dex_filt = dex_filter
        pokemon = pokemon_obj
        satisfies_criteria = True
        # GO through all criteria and eliminate (return false) when the filter no satisfied
        if dex_filter['type']:
            if not dex_filt['type'] in pokemon['type']:
                satisfies_criteria = False

        if dex_filter['min_catch']:
            if not pokemon['catchrate'] >= float(dex_filt['min_catch']):
                satisfies_criteria = False

        max_catch_bool = True
        if dex_filter['max_catch']:
            if not pokemon['catchrate'] <= float(dex_filt['max_catch']):
                satisfies_criteria = False

        min_hatch_bool = True
        if dex_filter['min_hatch']:
            if not pokemon['hatchtime'][1] >= float(dex_filt['min_hatch']):
                satisfies_criteria = False

        max_hatch_bool = True
        if dex_filter['max_hatch']:
            if not pokemon['hatchtime'][0] <= float(dex_filt['max_hatch']):
                satisfies_criteria = False

        min_weight_bool = True
        if dex_filter['min_weight']:
            if not pokemon['weight'] >= float(dex_filt['min_weight']):
                satisfies_criteria = False

        max_weight_bool = True
        if dex_filter['max_weight']:
            if not pokemon['weight'] <= float(dex_filt['max_weight']):
                satisfies_criteria = False

        min_height_bool = True
        if dex_filter['min_height']:
            if not pokemon['height'] >= float(dex_filt['min_height'])*100:
                print("min_height at fault")
                print(str(pokemon['height']) + " and " + str(float(dex_filt['min_height'])*100))
                satisfies_criteria = False

        if dex_filter['max_height']:
            if not pokemon['height'] <= float(dex_filt['max_height'])*100:
                satisfies_criteria = False

        return satisfies_criteria



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

    def getMovesOfType(self, type):
        data = self.getData("moves.json")
        data_of_type = {}
        for item in data:
            if type in data[item]['type'] :
                data_of_type[item]=data[item]
        return data_of_type

    def getMovesOfCategory(self, category):
        data = self.getData("moves.json")
        data_of_category = {}
        for item in data:
            if category in data[item]['category'] :
                data_of_category[item]=data[item]
        return data_of_category


    def getTypes(self):
        types = self.getData("poketypes.json")
        return types





    def getData(self, filename):
        with open(filename, "r") as read_file:
            return json.load(read_file)
