# Imported modules
import pickle

def unpickle(file_location):
    fo = open(file_location, 'rb')
    dict = pickle.load(fo, encoding='bytes')
    fo.close()
    return dict
