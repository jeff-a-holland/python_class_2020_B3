#!/Users/jeff/.pyenv/shims/python

import socket
import pickle

def main():
    def square_int():
        arg = 5
        arg_squared = arg * arg
        arg_dict = {arg: arg_squared}
        #print(f'\nSquared int dict object is:\n   {arg_dict}',
        #       'and is of type:', type(arg_dict))
        #pickled_obj = pickle.dumps(arg_dict)
        #print(f'\nPickled object is:\n   {pickled_obj}',
        #       '\n\nSending pickled object back to the client now...\n\n'
        #       '######################################################\n')
        #print(pickled_obj)
        #return pickled_obj
        print(arg_dict)

    square_int()

if __name__ == "__main__":
    main()
