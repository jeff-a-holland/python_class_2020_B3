#!/Users/jeff/.pyenv/shims/python

import socket
import sys

def send_client_message(client, argv_list):
    """Client program send_client_message function. Is passed the client socket
       object and the argv_list to process and send to the server for it to
       process and echo back, or send error information back via STDOUT.""
    """
    argv_list.pop(0)
    argv_str = ' '.join(argv_list)
    message = argv_str.encode('utf8')
    client.sendall(message)
    print(str(client.recv(4096), 'utf-8'))

def run_client(argv_list):
    """Client program run_client function. Starts up client socket connection
       to the server and sends socket object 'client' to the send_client_message
       function."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            server_ip = socket.gethostbyname('localhost')
            server_port = 9999
            client.connect((server_ip, server_port))
            send_client_message(client, argv_list)

    except socket.timeout as e:
        raise SystemExit(f'\n  Error connecting to remote socket: {e}\n'
                          'Exiting...\n')

def main():
    """Client program main. Run after server is started. Valid arguments are:
       (1) say <string> , (2) increment <interger> , (3) bye . Invalid arguments
       will be flagged as non-fatal errors logged to STDOUT and the program will
       continue. Sends argv_list with command line arguments to the run_client
       function."""
    argv_list = sys.argv
    run_client(argv_list)

if __name__ == "__main__":
    main()
