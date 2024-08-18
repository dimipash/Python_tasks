"""
Loads JSON data from 'load.json' file and pretty prints it.
"""

import pprint
import json

with open("load.json", "r") as f:
    data = json.load(f)

pprint.pprint(data)
