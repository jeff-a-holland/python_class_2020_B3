#!/Users/jeff/.pyenv/shims/python

import socket
import re

def get_client_connection(server):
    """Server program get_client_connection function. Prints out the client
       command if it was valid, otherwise print non-fatal error to STDOUT."""
    try:
        socket_object, client_ip = server.accept()
        with socket_object:
            while True:
                data = socket_object.recv(1024)
                if data:
                    socket_object.sendall(data)
                    client_message = (str(data.decode('utf-8')))
                    client_message_lowercase = (str.lower(data.decode('utf-8')))

                    if client_message_lowercase == 'bye':
                        print(client_message,'\n')
                        socket_object.close()
                        exit()

                    elif client_message_lowercase.startswith('increment'):
                        temp_list =list(client_message.split(' '))
                        cntr_value = temp_list[1]
                        try:
                            if isinstance(int(cntr_value), int):
                                cntr_value = int(cntr_value)
                                print (cntr_value + 1)
                        except ValueError as e:
                            print(f'\n  Non-fatal ValueError exception: {e}\n'
                                  '  The "increment" option only takes '
                                  'integers. Please try again.\n')

                    elif client_message_lowercase.startswith('say'):
                        client_message = \
                                   re.sub('^(?:say|SAY|Say|SAy|SaY|sAY|saY) {1,}',
                                          '', client_message)
                        print(client_message)

                    else:
                        print ('\n  Invalid message format sent from client!!\n'
                               f'  Message was: {client_message}\n\n'
                               '  Valid message formats are: \n'
                               '  - say <string> (e.g. say Hi!)\n'
                               '  - increment <integer value> '
                               '(e.g. increment 100)\n'
                               '  - bye (e.g. bye or Bye)\n\n'
                               '  Try again, please\n')

                else:
                    break

    except socket.error as e:
        raise SystemExit(f'Error getting client connection: {e}')

def run_server():
    """Server program run_server function. Calls get_client_connection function
       and supplies the socket object 'server' to it."""
    server_ip = socket.gethostbyname('localhost')
    listening_port = 9999
    print(f'\n  Binding socket to {server_ip} on port: {listening_port}\n  '
           'Wait one moment, please...')

    mssg_flag = False
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
                # SO_REUSEADDR flag tells the kernel to reuse a local socket
                # in TIME_WAIT state, without waiting for its natural timeout
                # to expire.
                server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                server.bind((server_ip, listening_port))
                server.listen()
                if not mssg_flag:
                    print('  Successful socket connection on port'
                          f'{listening_port}\n')
                    print('  Now accepting client messages!!\n')
                    mssg_flag = True
                get_client_connection(server)

        except socket.error as e:
            print('Client already bound to socket')

def main():
    """Server program main function. Calls run_server function."""
    run_server()

if __name__ == "__main__":
    main()
