import random

from phrase_list import Phrases

from fastapi import FastAPI

APIOps =  FastAPI()


@APIOps.get('/phrase')
def PhraseGenerator():
    n = random.randint(0,len(Phrases)-1)

    
    return {
    
    'Phrase':Phrases[n][0],
    'Author':Phrases[n][1]
    
    }