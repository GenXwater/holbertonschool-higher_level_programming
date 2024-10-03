#!/usr/bin/python3

import json

def serialize_and_save_to_file(data, filename):
    with open(filename, mode="w", encoding='utf-8') as file:
        return json.dump(data, file)

def load_and_deserialize(filename):
    with open(filename, mode="r", encoding='utf-8') as file:
        return json.load(file)
