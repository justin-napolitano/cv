#csv_log.py

#json_log.py
import csv
import logging

"""
begins the logging
"""
def log(dictionary):

    #with open(dictionary['log_dump'], 'w') as f:  # Just use 'w' mode in 3.x
    ##    w = csv.DictWriter(f, dictionary.keys())
    #    w.writeheader()
    #    w.writerow(dictionary)

    logging.basicConfig(level=logging.DEBUG, filename=dictionary['log_dump'])
    logging.debug('{}: {}'.format(dictionary['datetime'], str(dictionary)))