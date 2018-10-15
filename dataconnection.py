import json

class PokeData():
    def __len__(self):
        data = self.getPokedex()
        return len(data)

    def numByName(self, name):
        data = self.getPokedex()
        for item in data:
            if name.lower() == item['name'].lower():
                return item["dexnum"]


    def getPokedexOfType(self, type):
        data = self.getPokedex()
        data_of_type = []
        for item in data:
            if type in item['type'] :
                data_of_type.append(item)
        return data_of_type

    def getFilteredPokedex(self, dex_filter):
        dex = self.getPokedex()
        filtered_dex = []
        for pokemon in dex:
            if self.passesDexFilter(pokemon, dex_filter):
                filtered_dex.append(pokemon)
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
                satisfies_criteria = False

        if dex_filter['max_height']:
            if not pokemon['height'] <= float(dex_filt['max_height'])*100:
                satisfies_criteria = False

        return satisfies_criteria



    def getEvolutionsOf(self, num):
        data = self.getPokedex()
        evolutions = []
        for evolution in self.attributeByNum("evolutions", num):
            for item in data:
                if evolution == item['name']:
                    evolutions.append(item)
        return evolutions

    def getPokeByNum(self,num):
        data = self.getPokedex()
        poke = {}
        for item in data:
            if item['dexnum'] == num:
                poke = item
        return poke

    def nameByNum(self, num):
        return self.attributeByNum("name", num)

    def attributeByNum(self, attribute, num):
        data = self.getPokedex()
        poke = self.getPokeByNum(num)
        value = poke[attribute]
        return value


    def getPokedexOfMove(self, move):
        dex = self.getPokedex();
        altered_dex = []
        for pokemon in dex:
            if move in pokemon['moves']:
                altered_dex.append(pokemon)
        return altered_dex

    def getMove(self, move):
        moves = self.getMoves()
        for item in moves:
            if item['name'] == move:
                return item
        return None

    def fillMovesArray(self, moves_array):
        moves = moves_array;
        new_moves_array = []
        all_moves = self.getMoves()
        for move in all_moves:
            if move['name'] in moves:
                new_moves_array.append(move)
        return new_moves_array


    def getMovesOfType(self, type):
        data = self.getMoves()
        data_of_type = []
        for item in data:
            if type in item['type'] :
                data_of_type.append(item)
        return data_of_type

    def getMovesOfCategory(self, category):
        data = self.getMoves()
        data_of_category = []
        for item in data:
            if category in item['category'] :
                data_of_category.append(item)
        return data_of_category



    def getPokedex(self):
        data = self.getData("pokemons_updated.json")
        return data

    def getTypes(self):
        types = self.getData("poketypes.json")
        return types

    def getMoves(self):
        data = self.getData("moves_updated.json")
        return data

    def getData(self, filename):
        with open(filename, "r") as read_file:
            return json.load(read_file)
