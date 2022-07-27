
import requests
from requests import request
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pokemon_search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        pn = request.form.get("pokemon")
        get_pokemon_info = f"https://pokeapi.co/api/v2/pokemon/{pn}"
        response = requests.get(get_pokemon_info)
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
        return render_template('search.html', pokemon_info = pokemon_info)
    return render_template('search.html')
   


if __name__ == '__main__':
    app.run()