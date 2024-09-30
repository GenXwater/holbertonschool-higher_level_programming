#!/usr/bin/python3
"""
Learn JSON
"""

import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"

"""
Charger la liste à partir du fichier s'il existe et s'il n'est pas vide
sinon créer une liste vide
"""
try:
    my_list = load_from_json_file(filename)
except (FileNotFoundError, ValueError):
    my_list = []

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)
