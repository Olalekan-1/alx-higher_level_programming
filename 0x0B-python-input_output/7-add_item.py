#!/usr/bin/python3
""" scripts that load a json, file add to the list
and save a again to json.
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = argv

filename = "add_item.json"
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

for i in range(1, len(arguments)):
    my_list.append(arguments[i])

save_to_json_file(my_list, filename)
