#!/Users/jeff/.pyenv/shims/python

import socket
import sys
import re
import pickle
import codecs

class RunClient(object):
    """RunClient class for module"""
    def __init__(self, argv_list, ip, port):
        self.argv_list = argv_list
        self.ip = ip
        self.port = port

    def send_client_message(self, client):
        """Client program send_client_message method. Is passed the client socket
           object and the argv_list to process and send to the server for it to
           process and echo back, or send error information back via STDOUT.""
        """
        self.argv_list.pop(0)
        if len(self.argv_list) <= 1 and str.lower(self.argv_list[0]) != 'bye':
            print('\n  ERROR. No argument(s) supplied.\n  Enter the name of the'
                  ' function to run on the server and at least\n  one argument '
                  'of the proper type, depending on the function name '
                  'supplied.\n  Please try again.\n')
            exit()

        elif self.argv_list[0] == 'reverse_words' and \
                         re.match(r"[-+]?\d+$", self.argv_list[1]) is not None:
            print('\n  ERROR. The function name "reverse_words" requires a'
                  ' string of words.\n  Please try again.\n')
            exit()

        elif self.argv_list[0] == 'square_int' and \
                             re.match(r"[-+]?\d+$", self.argv_list[1]) is None:
            print('\n  ERROR. The function name square_int requires an int.'
                  '\n  Please try again.\n')
            exit()

        elif self.argv_list[0] == 'square_int' and len(self.argv_list) > 2:
            print('\n  ERROR. The function name square_int only takes one int'
                  ' as an argument.\n  Please try again.\n')
            exit()

        elif self.argv_list[0] != 'square_int' and \
             self.argv_list[0] != 'reverse_words' and \
             str.lower(self.argv_list[0]) != 'bye':
            print('\n  ERROR. That function does not exist on the server.'
                  '\n  Please try again.\n')
            exit()

        argv_str = ' '.join(self.argv_list)
        message = argv_str.encode('utf8')
        client.sendall(message)

        if str.lower(self.argv_list[0]) != 'bye':
            pickled_object = client.recv(4096)
            unpickled_object = pickle.loads(pickled_object)
            print('\n  Unpickled Object type:', type(unpickled_object))
            print(f'  Unpickled Object: {unpickled_object}\n')
        else:
            print(str(client.recv(4096), 'utf-8'))


    def run_client(self, c):
        """Client run_client method. Starts up client socket connection
           to the server and sends socket object 'client' to the
           send_client_message function.
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                server_ip = self.ip
                server_port = self.port
                client.connect((server_ip, server_port))
                c.send_client_message(client)

        except socket.timeout as e:
            raise SystemExit(f'\n  Error connecting to remote socket: {e}\n'
                              'Exiting...\n')

def main():
    """Client program main. Instantiates RunClient object and then calls the
       run_client method, which calls send_client_message method. Run after
       server is started. Valid arguments are the name of a function to invoke
       and its argument(s), or, the command 'bye' to end the connection to the
       server. Functions and their arg are:
       (1) reverse_words <string of space delimited words>
       OR
       (2) square_int <interger>

       The server will respond with the a the output of the server's function by
       that name, which will be pickled and of a data type defined in the
       function. For example, "reverse_words good morning" will return a pickled
       list ['morning', 'good'], and square_int will return the pickled dict
       {5: 25}.

       Invalid arguments will be flagged as fatal errors and the client will
       exit and a message will be logged to STDOUT. The server will continue
       to listen for proper client messages on port 9999/TCP.
   """
    argv_list = sys.argv
    c = RunClient(argv_list, '127.0.0.1', 9999)
    c.run_client(c)

if __name__ == "__main__":
    main()
