from flask import Flask, request, render_template, redirect
from dataconnection import PokeData
import random


app = Flask(__name__)
pokedata = PokeData()

abcd = pokedata.getPokedex()
times = []
for abc in abcd:
    times.append((abcd[abc]["height"]))

times.sort()
print(times)



app.route('/force500')
def force500():
    abort(500)

app.route('/force404')
def force500():
    abort(404)

# ROUTE HANDLING
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def create_search_url():
    searched_phrase = request.args.get('search')
    return redirect("/search/{}".format(searched_phrase))

@app.route('/search/<search_word>')
def search(search_word):
    return 'Search page. Searched word: {}'.format(search_word)

@app.route('/pokedex')
def pokedex():
    data = pokedata.getPokedex()
    typeslist = pokedata.getTypes()
    return render_template('pokedex.html', pokemon_list = data, poketypes = typeslist)

@app.route('/pokemon')
def redir_to_pokedex():
    return redirect("/pokedex")

@app.route('/pokemon/random')
def random_pokemon():
    number_of_pokemon = len(pokedata)
    dexnum = random.randint(1,number_of_pokemon)
    pokemon_name = pokedata.nameByNum(dexnum)
    return redirect("/pokemon/{}".format(pokemon_name))


@app.route('/pokemon/<name>')
def pokemon(name):
    dexnum = pokedata.numByName(name)
    if not dexnum:
        return render_template("err404.html", errorcode = 404)
    pokemon = pokedata.getPokeByNum(dexnum)
    evolutions = pokedata.getEvolutionsOf(dexnum)
    return render_template('pokepage.html', pokemon = pokemon, evolutions = evolutions)
    # return "<img src='/static/images/{}' >".format(img)

@app.route('/types')
def poketypes():
    types = pokedata.getTypes()
    return render_template("types.html", poketypes = types)

@app.route('/types/<type>')
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
    return render_template("moves_pokedex.html", pokemon_list = data, move = move_obj)

# @app.route('/kanto')
# def kanto():
#     return render_template("kanto.html")

@app.errorhandler(404)
def page_not_found(err):
    return render_template('err404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)
