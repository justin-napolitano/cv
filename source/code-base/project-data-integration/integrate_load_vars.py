#load_vars.py
import os
import datetime
import yaml
import glob
import datetime

def load_stream():
    #print("test")
    stream = open("config.yaml", 'r')
    dictionary = yaml.load(stream)
    return dictionary

def load_paths(dictionary):
    dictionary['directories']['cwd'] = os.getcwd()
    #print(dictionary['directories']['cwd'])
    dictionary['directories']['input_directory'] = os.sep.join((dictionary['directories']['cwd'],'input', dictionary['directories']['input_directory']))
    #print(dictionary['directories']['input_directory'])
    dictionary['directories']['output_directory'] = os.sep.join((dictionary['directories']['cwd'],'output', dictionary['directories']['output_directory']))
    dictionary['files']['json_dump'] = os.sep.join((dictionary['directories']['cwd'], dictionary['directories']['json_dump_directory'], dictionary['files']['json_dump_filename']))
    dictionary['files']['log_dump'] = os.sep.join((dictionary['directories']['cwd'], dictionary['directories']['csv_log_directory'], dictionary['files']['csv_log_filename']))
    dictionary['directories']['read_directory'] = os.sep.join((dictionary['directories']['cwd'],'output',dictionary['directories']['read_directory']))
    return True

def load_files(dictionary):
    os.chdir(dictionary['directories']['input_directory'])
    dictionary['files']['files_to_merge'] = [i for i in glob.glob('*.{}'.format(dictionary['files']['input_extension']))]
    os.chdir(dictionary['directories']['cwd'])
    return True

def load_date(dictionary):
    dictionary['vars']['date'] = str(datetime.date.today())
    dictionary['vars']['datetime']=str(datetime.datetime.now())
    return True


