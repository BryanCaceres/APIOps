import random

from phrases_list import Phrases
from fastapi import FastAPI

app =  FastAPI()

@app.get('/')
def PhraseGenerator():
    
    n = random.randint(0,len(Phrases)-1)

    
    return {
    
    'Phrase':Phrases[n][0],
    'Author':Phrases[n][1]
    
    }