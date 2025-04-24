import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0891a6b91b1600caa946a9509db4f0e4'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_newpokemon = {
    "name": "Бульба",
    "photo_id": 4
}

response_newpokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_newpokemon)
print(response_newpokemon.json())

pokemon_id = response_newpokemon.json()['id']
body_newname = {
    "pokemon_id": pokemon_id,
    "name": "Пикачу",
    "photo_id": 2
}

response_newname = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_newname)
print(response_newname.json())

body_catch = {
    "pokemon_id": pokemon_id
}

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.json())
