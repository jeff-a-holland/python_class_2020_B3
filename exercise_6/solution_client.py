#!/Users/jeff/.pyenv/shims/python

import socket
import sys
import re
import pickle

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
        if len(self.argv_list) > 2:
            print('\n   Too many arguments supplied.\n   Enter the name of the '
                  'function to run on the server and one argument of the '
                  'proper type.\n')

        elif self.argv_list[0] == 'translate_word' and \
                         re.match(r"[-+]?\d+$", self.argv_list[1]) is not None:
            print('\n  The function name translate_word requires a string.'
                  ' Please try again.\n')

        elif self.argv_list[0] == 'square_int' and \
                             re.match(r"[-+]?\d+$", self.argv_list[1]) is None:
            print('\n  The function name square_int requires an int.'
                  ' Please try again.\n')

        elif self.argv_list[0] != 'square_int' and self.argv_list[0] != 'translate_word':
            print('\n  That function does not exist on the server. Please try again.\n')

        argv_str = ' '.join(self.argv_list)
        message = argv_str.encode('utf8')
        client.sendall(message)
        print(str(client.recv(4096), 'utf-8'))

    def run_client(self, c):
        """Client run_client method. Starts up client socket connection
           to the server and sends socket object 'client' to the send_client_message
           function.
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
       and it's argument, or, the command 'bye' to end the connection to the
       server. Functions and their arg are:
       (1) translate_word <string>
       OR
       (2) square_int <interger>

       The server will respond with the a the output of the server's function by
       that name, which will be pickled and of a data type defined in the
       function. For example, "translate_word hola" will return a pickled list
       with the values "hola" and "hello", and square_int will return a
       pickled dict with the key "5" and the value "25".

       Invalid arguments will be flagged as non-fatal errors logged to STDOUT
       and the program will continue.
   """
    argv_list = sys.argv
    c = RunClient(argv_list, '127.0.0.1', 9999)
    c.run_client(c)

if __name__ == "__main__":
    main()
