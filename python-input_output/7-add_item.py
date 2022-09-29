#!/usr/bin/python3
"""Script to add arguments to a Python list
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    items_list = []
    try:
        items_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        pass
    for i in range(1, len(sys.argv)):
        items_list.append(sys.argv[i])
    save_to_json_file(items_list, 'add_item.json')


if __name__ == '__main__':
    main()
