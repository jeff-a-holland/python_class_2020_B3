#!/Users/jeff/.pyenv/shims/python

import socket
import re

class RunServer(object):
    """RunServer Class for module"""
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def get_client_connection(self, server):
        """RunServer get_client_connection method. Prints out the client
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
                            print(client_message)
                            socket_object.close()
                            exit()

                        elif client_message_lowercase.startswith('increment'):
                            temp_list =list(client_message.split(' '))
                            cntr_value = temp_list[1]
                            try:
                                if isinstance(int(cntr_value), int):
                                    client_message = int(cntr_value) + 1
                                    print(client_message)
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

    def run_server(self, s):
        """Server program run_server method."""
        server_ip = self.ip
        server_port = self.port
        print(f'\n  Binding socket to {server_ip} on port: {server_port}\n  '
               'Wait one moment, please...')

        mssg_flag = False
        while True:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.server:
                    # SO_REUSEADDR flag tells the kernel to reuse a local socket
                    # in TIME_WAIT state, without waiting for its natural timeout
                    # to expire.
                    self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    self.server.bind((server_ip, server_port))
                    self.server.listen()
                    if not mssg_flag:
                        print('  Successful socket connection on port'
                              f' {server_port}\n')
                        print('  Now accepting client messages!!\n')
                        mssg_flag = True
                    s.get_client_connection(self.server)

            except socket.error as e:
                print('Client already bound to socket')

def main():
    """Server program main function. Instatiates class object and then calls
       run_server method of the class, which calls get_client_connection class"""
    s = RunServer('127.0.0.1', 9999)
    s.run_server(s)

if __name__ == "__main__":
    main()
