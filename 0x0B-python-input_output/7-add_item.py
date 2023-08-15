#!/usr/bin/python3
"""define ajson file writting function."""
import json

def save_to_json_file(my_obj, filename)
   """write an object with atext file usig json representation"""
   with open(filename, "w") as f:
       json.dump(my_obj, f)
