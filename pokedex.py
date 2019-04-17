from flask import Flask, request, render_template, redirect, abort
from dataconnection import PokeData
import random


app = Flask(__name__)
pokedata = PokeData()


app.route('/force500')
def force500():
    return abort(500)

app.route('/force404')
def force500():
    return abort(404)

# ROUTE HANDLING
@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/search')
# def create_search_url():
#     searched_phrase = request.args.get('search')
#     return redirect("/search/{}".format(searched_phrase))
#
# @app.route('/search/<search_word>')
# def search(search_word):
#     return 'Search page. Searched word: {}'.format(search_word)

@app.route('/pokemon')
def red_pokedex():
    return redirect("/pokedex")

@app.route('/pokedex')
def pokedex():
    dex_filter = {}
    data = []
    filter_on = False
    if request.args:
        dex_filter = make_filter()
        data = pokedata.getFilteredPokedex(dex_filter)
        filter_on = True
    else:
        data = pokedata.getPokedex()
    typeslist = pokedata.getTypes()
    return render_template('pokedex.html', pokemon_list = data, poketypes = typeslist, last_filter= dex_filter, filter_on = filter_on)

def make_filter():
    dex_filter = {}
    dex_filter['type'] = request.args.get('type')
    dex_filter['min_catch'] = request.args.get('min_catch')
    dex_filter['max_catch'] = request.args.get('max_catch')
    dex_filter['min_hatch'] = request.args.get('min_hatch')
    dex_filter['max_hatch'] = request.args.get('max_hatch')
    dex_filter['min_weight'] = request.args.get('min_weight')
    dex_filter['max_weight'] = request.args.get('max_weight')
    dex_filter['min_height'] = request.args.get('min_height')
    dex_filter['max_height'] = request.args.get('max_height')
    return dex_filter

@app.route('/pokedex/<passed_var>')
def redir_to_pokemon(passed_var):
    pokedex = pokedata.getPokedex()
    passed_a_num = True;
    try:
        int(passed_var)
    except ValueError:
        passed_a_num = False

    if passed_a_num and int(passed_var) in range(1,152) :
        pokemon_name = pokedata.getPokeByNum(int(passed_var))['name']
        return redirect("/pokemon/{}".format(pokemon_name))
    else:
        for pokemon in pokedex:
            if pokemon['name'].lower() in str(passed_var).lower():
                return redirect("/pokemon/{}".format(pokemon['name']))
    return abort(404)


@app.route('/pokemon/random')
def random_pokemon():
    number_of_pokemon = len(pokedata)
    dexnum = random.randint(1,number_of_pokemon)
    pokemon_name = pokedata.nameByNum(dexnum)
    return redirect("/pokemon/{}".format(pokemon_name))


@app.route('/pokemon/<name>')
def pokemon(name):
    # Check if the name variable is a number, if yes > redirect
    passed_a_num = True;
    try:
        int(name)
    except ValueError:
        passed_a_num = False

    if passed_a_num and int(name) in range(1,152) :
        return redirect("/pokemon/{}".format(pokedata.nameByNum(int(name))))
    else:
        dexnum = pokedata.numByName(name)

    #if the dexnum is not set to a valid dexnum throw 404
    if not dexnum:
        return render_template("err404.html", errorcode = 404)

    # logic for getting next and previous pokemon
    pokemon = pokedata.getPokeByNum(dexnum)
    if dexnum == 1:
        prev_pokemon = {}
        next_pokemon = pokedata.getPokeByNum(dexnum+1)
    elif dexnum == 151:
        prev_pokemon = pokedata.getPokeByNum(dexnum-1)
        next_pokemon = {}
    else:
        prev_pokemon = pokedata.getPokeByNum(dexnum-1)
        next_pokemon = pokedata.getPokeByNum(dexnum+1)
    evolutions = pokedata.getEvolutionsOf(dexnum)
    moves = pokedata.fillMovesArray(pokemon['moves'])
    return render_template('pokepage.html', pokemon = pokemon, prev_pokemon = prev_pokemon, next_pokemon = next_pokemon, evolutions = evolutions, moves = moves)
    # return "<img src='/static/images/{}' >".format(img)

@app.route('/pokemon/types')
def poketypes():
    types = pokedata.getTypes()
    return render_template("types.html", poketypes = types)

@app.route('/pokemon/types/<type>')
def poketype(type):
    # making use of the pokedex template with one extra variable - the type (filter)
    data = pokedata.getPokedexOfType(type)
    typeinfo = pokedata.getTypes()[type]['description']
    return render_template('typed_pokedex.html', pokemon_list = data, type = type, typeinfo = typeinfo)

@app.route("/moves")
def pokemoves():
    moves = pokedata.getMoves()
    return render_template("moves.html", pokemoves = moves)

@app.route("/moves/<move>")
def pokemove(move):
    data = pokedata.getPokedexOfMove(move)
    move_obj = pokedata.getMove(move)
    if not move_obj:
        return abort(404)
    return render_template("moves_pokedex.html", pokemon_list = data, move = move_obj)

@app.route('/moves/types/<type>')
def pokemovetype(type):
    data = pokedata.getMovesOfType(type)
    if not data:
        return abort(404)
    return render_template('typed_moves.html', pokemoves= data, type = type)

@app.route('/moves/categories/<category>')
def pokemovecategory(category):
    data = pokedata.getMovesOfCategory(category)
    if not data:
        return abort(404)
    return render_template('categorised_moves.html', pokemoves= data, category = category)


# @app.route('/kanto')
# def kanto():
#     return render_template("kanto.html")

@app.errorhandler(404)
def page_not_found(err):
    return render_template('err404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)
