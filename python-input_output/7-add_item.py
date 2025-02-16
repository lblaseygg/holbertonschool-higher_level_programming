#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a file."""

import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing list if the file exists, otherwise start with an empty list
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add command-line arguments (excluding script name) to the list
my_list.extend(sys.argv[1:])

# Save updated list to JSON file
save_to_json_file(my_list, filename)
