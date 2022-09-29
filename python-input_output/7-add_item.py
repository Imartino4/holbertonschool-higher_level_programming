#!/usr/bin/python3
"""Script to add arguments to a Python list
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    list = load_from_json_file(filename)
    for i in range(1, len(sys.argv)):
        list.append(sys.argv[i])
    save_to_json_file(list, filename)
except Exception:
    list = []
    for i in range(1, len(sys.argv)):
        list.append(sys.argv[i])
    save_to_json_file(list, filename)
