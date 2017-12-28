import json, io
from random import randint
import os

def random_digits(oneliners_size):
    # Return a joke index between first and last joke in data
    return randint(0, oneliners_size-1)

def getOneLiner():
    # Read JSON file
    with open('data.json') as data_file:
        data_loaded = json.load(data_file)

    oneliner = data_loaded['oneliners'][random_digits(len(data_loaded['oneliners']))]

    print oneliner

    ret_this = json.dumps({'oneliner' : oneliner})
    return ret_this
