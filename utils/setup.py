
from random import randint
import json

def image_url():
	with open('./assets/data/gifs.json', 'r', encoding="utf-8") as data:
		image_urls = json.load(data)


	n = randint(0, len(image_urls["jail"]))
	return image_urls["jail"][n]


print(image_url())