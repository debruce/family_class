import pickle
import yaml
from termcolor import colored
import json
from pprint import pprint

with open('names.json', "w") as nfile:
    d = {
        
        'Evie': 'Berghost',
        'Weronika': 'Nowak',
        'Artemis': 'Grigg'
    
    }
    json.dump(d, nfile)

with open ('names.json', "r") as rfile:
    a = json.load(rfile)
    for cnt, i in enumerate(a):
        print(cnt, i)

