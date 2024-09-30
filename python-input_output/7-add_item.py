#!/usr/bin/python3
import sys
from os import path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

"""
Charger la liste à partir du fichier s'il existe et s'il n'est pas vide
sinon créer une liste vide
"""
if path.exists(filename) and path.getsize(filename) > 0:
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)
