from unittest import result
from urllib import response
from django.shortcuts import render
import requests 
import hashlib
import json 
from pprint import pprint
from models import personaje
# Create your views here.
private = 'f9320751574fc57064cbbd2ce85e7da0e8d35e1a' 
ts= '1'
public = '2b1057df128704bfa3b850522c753ae1'
hash = hashlib.md5((ts + private + public).encode()).hexdigest()

characters = requests.get(f"http://gateway.marvel.com/v1/public/characters?ts={ts}&apikey={public}&hash={hash}")
#characters = requests.get(base + 'characters',
 #             params={'apikey':public,
#				    'ts':ts,
#					'hash':hash}).json()
if characters.status_code == 200: 
    response_json = json.loads(characters.text)
    for i in response_json["data"]["results"]:
        pj = personaje(
            id = i['id']
            nombre = i['name']
            descripcion = i['description']
            imagen = i['thumbnail']['path']
            extension = i['thumbnail']['extension']
        )

        pj.save()
#pprint(infP)
#for i in infP:
#	pprint(infP)