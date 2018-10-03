from flask import Flask, request, render_template, redirect
from dataconnection import PokeData
import random


app = Flask(__name__)
pokedata = PokeData()

# ROUTE HANDLING
@app.route('/')
def index():
    return 'Index page'

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
    img = pokedata.imgByNum(dexnum)
    pokemon = pokedata.getPokeByNum(dexnum)
    return render_template('pokepage.html', pokemon = pokemon)
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

if __name__ == '__main__':
	app.run(debug=True)
