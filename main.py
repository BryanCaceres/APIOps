import random

from phrase_list import Phrases

from fastapi import FastAPI

app =  FastAPI()


@app.get('/')
def PhraseGenerator():
    Phrases = [

    ['Cuanto más grande es la dificultad, más gloria hay en superarla','Epícuro'],
    ['La vida debe ser comprendida hacia atrás. Pero debe ser vivida hacia delante','Søren Kierkegaard'],
    ['El hombre valiente es el que no solo supera a sus enemigos, sino también a sus placeres','Demócrito'],
    ['La creatividad requiere que la valentía se desprenda de las certezas','Erich Fromm'],
    ['Aquellos que no conocen la historia están condenados a repetirla','Edmund Burke']
    ]
    n = random.randint(0,len(Phrases)-1)

    
    return {
    
    'Phrase':Phrases[n][0],
    'Author':Phrases[n][1]
    
    }