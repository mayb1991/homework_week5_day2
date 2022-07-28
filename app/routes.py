from app import app
from flask import render_template, request
import requests

from app.forms import PokemonSearchForm

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pokemon_search', methods=['GET', 'POST'])
def search():
    form = PokemonSearchForm()
    pokemon_info = {}
    if request.method == 'POST':
        pn = form.name.data


        get_pokemon_info = f"https://pokeapi.co/api/v2/pokemon/{pn}"
        response = requests.get(get_pokemon_info)
        if response.ok:
            data = response.json()
            pokemon_info = {
                'name': data['forms'][0]['name'],
                'abilities': data['abilities'][1]['ability']['name'],
                'base_exp': data['base_experience'],
                'sprite': data['sprites']['front_shiny'],
                'attack': data['stats'][1]['base_stat'],
                'h_p': data['stats'][0]['base_stat'],
                'def': data['stats'][2]['base_stat']
            }
        print(pokemon_info)
        return render_template('search.html',form=form, pokemon_info = pokemon_info)
    return render_template('search.html',form=form, pokemon_info = pokemon_info)
   