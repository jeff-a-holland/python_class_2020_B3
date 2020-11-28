#!/Users/jeff/.pyenv/shims/python

import socket
import sys

class RunClient(object):
    """RunClient class for  module"""
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
        argv_str = ' '.join(self.argv_list)
        message = argv_str.encode('utf8')
        client.sendall(message)
        print(str(client.recv(4096), 'utf-8'))

    def run_client(self, c):
        """Client run_client method. Starts up client socket connection
           to the server and sends socket object 'client' to the send_client_message
           function."""
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
       server is started. Valid arguments are:
       (1) say <string> , (2) increment <interger> , (3) bye . Invalid arguments
       will be flagged as non-fatal errors logged to STDOUT and the program will
       continue. Sends argv_list with command line arguments to the run_client
       function."""
    argv_list = sys.argv
    c = RunClient(argv_list, '127.0.0.1', 9999)
    c.run_client(c)

if __name__ == "__main__":
    main()
