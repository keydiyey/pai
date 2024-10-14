from random import randint
import json



def load(PATH):
    with open(PATH, 'r', encoding="utf-8") as data:
        image_urls = json.load(data)
    return image_urls

def get_jail_gif():
    image_urls = load('./assets/data/gifs.json')
    n = randint(0, len(image_urls["jail"])-1)
    
    return image_urls["jail"][n]