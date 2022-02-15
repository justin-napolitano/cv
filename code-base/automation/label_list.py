from distutils.command.build import build


try:
  import cPickle as pickle
except:
  import pickle

"""
A simple program that lists all of the labels that sphinx creates during a build.   It reads a pickle filen and prints the relevent dictionary.  
"""


def main():

    """"
    the pickle filen using this build as an example
    """
    PICKLE_FILE = "/Users/jnapolitano/Dropbox/python/Projects/websites/jnapolitano.io/build/doctrees/environment.pickle"

    #dat = pickle.load(PICKLE_FILE)

    #print(dat.domaindata['std']['labels'].keys())

    """"
    prints the laels from the domain data labels dictionary
    """
    for item in read_from_pickle(PICKLE_FILE):
        print(item.domaindata['std']['labels'].keys())
        print('/n')

""""
yields from pickle and passes it back to the print function.  Stops when eof is hit.
"""
def read_from_pickle(path):
    with open(path, 'rb') as file:
        try:
            while True:
                yield pickle.load(file)
        except EOFError:
            pass



if __name__ == "__main__":
    main()

    