#log.py

import json
import csv
import logging
import gc

"""
json and csv log dumps.  
"""

"""
Garbage collector investigation.
"""
class garbage_collector:
    def __init__(self, name):
        self.name = name
        self.id = 0
        self.isalive = 1

    def enable_collection(self):
        gc.enable()
        gc.set_debug(gc.DEBUG_LEAK)
    
    def get_objects(self):
        self.objects = gc.get_objects()
    
    def get_garbage(self):
        self.garbage = gc.garbage()

    def get_stats(self):
        self.stats = gc.get_stats()

    def get_debug(self):
        self.debug_info = gc.get_debug()
    
    def collect():
        gc.collect

    

def json_dump(dictionary):
    #print(dictionary)
    with open(dictionary['files']['json_dump'], "w") as outfile: 
        json.dump(dictionary, outfile) 

def df(df, dictionary):
    dictionary['files']['json_dump2'] = dictionary['files']['json_dump'] + "2"
    df.to_json(dictionary['files']['json_dump2'])

def csv_dump(dictionary):

    #with open(dictionary['log_dump'], 'w') as f:  # Just use 'w' mode in 3.x
    ##    w = csv.DictWriter(f, dictionary.keys())
    #    w.writeheader()
    #    w.writerow(dictionary)

    logging.basicConfig(level=logging.DEBUG, filename=dictionary['files']['log_dump'])
    logging.debug('{}: {}'.format(dictionary['vars']['datetime'], str(dictionary)))