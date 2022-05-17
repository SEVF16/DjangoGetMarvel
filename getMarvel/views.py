
from urllib import response
import requests
from django.shortcuts import render
from getMarvel.models import personaje
from pprint import pprint
import service


#from .models import personaje
# Create your views here.

  
pj = service.get(requests)
characters = "'!?"
for i in pj:
    id = i['id'], 
    nombre =i['name'],
    descripcion = i['description'],
    imagen = i['thumbnail']['path'],
    extension =  i['thumbnail']['extension']
    
    imagen = ''.join( x for x in imagen if x not in characters)
    
    
    pj = personaje(
        id = id,
        nombre = nombre,
        descripcion = descripcion,
        imagen = imagen,
        extension = extension
    )
    
    pj.save()

    
'''
private = 'f9320751574fc57064cbbd2ce85e7da0e8d35e1a' 
ts= '1'
public = '2b1057df128704bfa3b850522c753ae1'
hash = hashlib.md5((ts + private + public).encode()).hexdigest()

characters = requests.get(f"http://gateway.marvel.com/v1/public/characters?ts={ts}&apikey={public}&hash={hash}")
    #characters = requests.get(base + 'characters',
    #             params={'apikey':public,
    #				    'ts':ts,
    #	
    #'hash':hash}).json()

if characters.status_code == 200: 
    response_json = json.loads(characters.text) 
    for i in response_json["data"]["results"]:
        id = i['id'], 
        nombre =i['name'],
        descripcion = i['description'],
        imagen = i['thumbnail']['path'],
        extension =  i['thumbnail']['extension']
        pj = personaje(
            id = id,
            nombre = nombre,
            descripcion = descripcion,
            imagen = imagen,
            extension = extension
        )

        pj.save()'''
        

'''def guardar (pj):
    perj = personaje(
        id = pj[0],
        nombre = pj[1],
        descripcion = pj[2],
        imagen = pj[3],
        extension = pj[4]
        )
    perj.save()'''

    

#pprint(infP)
#for i in infP:
#	pprint(infP)