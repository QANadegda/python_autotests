import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0891a6b91b1600caa946a9509db4f0e4'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '30463'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response.status_code == 200