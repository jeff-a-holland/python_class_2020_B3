#!/Users/jeff/.pyenv/shims/python

import socket
import sys

def send_client_message(s, argv_list):
    argv_list.pop(0)
    argv_str = ' '.join(argv_list)
    message = argv_str.encode('utf8')
    s.sendall(message)
    print(str(s.recv(4096), 'utf-8'))

def run_client(argv_list):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            server_ip = socket.gethostbyname('localhost')
            server_port = 9999
            s.connect((server_ip, server_port))
            send_client_message(s, argv_list)

    except socket.timeout as e:
        raise SystemExit(f'\n  Error connecting to remote socket: {e}\n  Exiting...\n')

def main():
    argv_list = sys.argv
    run_client(argv_list)

if __name__ == "__main__":
    main()
