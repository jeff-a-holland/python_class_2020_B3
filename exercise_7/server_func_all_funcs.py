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

def square_int(self, arg):
    self.arg = arg
    arg = int(arg[0])
    arg_squared = arg * arg
    arg_dict = {arg: arg_squared}
    print(f'\nSquared int dict object is:\n   {arg_dict}',
           'and is of type:', type(arg_dict))
    pickled_obj = pickle.dumps(arg_dict)
    print(f'\nPickled object is:\n   {pickled_obj}',
           '\n\nSending pickled object back to the client now...\n\n'
           '######################################################\n')
    return pickled_obj
