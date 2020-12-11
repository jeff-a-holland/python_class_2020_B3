#!/Users/jeff/.pyenv/shims/python

import socket
import pickle

def reverse_words(self, arg):
    self.arg = arg
    arg.reverse()
    print(f'\nReversed list object is:\n   {arg}',
           'and is of type:', type(arg))
    pickled_obj = pickle.dumps(arg)
    print(f'\nPickled object is:\n   {pickled_obj}',
           '\n\nSending pickled object back to the client now...\n\n'
           '######################################################\n')
    return pickled_obj
