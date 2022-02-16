#json_log.py
import json

"""
dumps the log as json
"""
def json_dump(dictionary):
    with open(dictionary['json_dump'], "w") as outfile: 
        json.dump(dictionary, outfile) 