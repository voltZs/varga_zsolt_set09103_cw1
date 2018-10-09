from flask import Flask, request, render_template, redirect
from dataconnection import PokeData
import random


app = Flask(__name__)
pokedata = PokeData()

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
    return render_template('pokedex.html', pokemon_list = data)

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
    img = pokedata.imgByNum(dexnum)
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
    return render_template('typed_pokedex.html', pokemon_list = data, type = type)

@app.route('/kanto')
def kanto():
    return render_template("kanto.html")

@app.errorhandler(404)
def page_not_found(err):
    return render_template('err404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)
