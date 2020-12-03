#!/Users/jeff/.pyenv/shims/python

import socket
import re
import pickle

class RunServer(object):
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
                        socket_object.sendall(b'111')
                        client_message = (str(data.decode('utf-8')))
                        client_message_lowercase = (str.lower(data.decode('utf-8')))

                        if client_message_lowercase == 'bye':
                            print(client_message)
                            socket_object.close()
                            exit()

                        elif client_message_lowercase.startswith('square_int'):
                            temp_list = list(client_message.split(' '))
                            int_value = temp_list[1]
                            try:
                                if isinstance(int(int_value), int):
                                    pass
                            except ValueError as e:
                                print(f'\n  Non-fatal ValueError exception: {e}\n'
                                      '  The "square_int" option only takes '
                                      'integers. Please try again.\n')

                        elif client_message_lowercase.startswith('translate_word'):
                            client_message = re.sub('^[a-zA-z]* {1,}', '', client_message)
                            if re.match(r"[-+]?\d+$", client_message) is None:
                                pass
                            else:
                                print('\n  Non-fatal ValueError exception: '
                                      f'The int "{client_message}" is not a string.\n'
                                      '  The "translate_word" option only takes'
                                      ' a string. Please try again.\n')

                        else:
                            print ('\n  Invalid function name and arg format '
                                   'sent from client!!\n'
                                   f'  Function and arg was: {client_message}\n\n'
                                   '   Valid functions and their args are:\n'
                                   '   (1) translate_word <string>  (e.g. translate_word hola)\n'
                                   '   OR\n'
                                   '   (2) square_int <interger>  (e.g. square_int 5)\n'
                                   '   OR\n'
                                   '   bye (e.g. bye or Bye)\n\n'
                                   '  Try again, please\n')

                    else:
                        break

        except socket.error as e:
            raise SystemExit(f'Error getting client connection: {e}')
        return client_message_lowercase

    def process_message(self, s, command):
        self.command = command
        self.s = s
        print(f'Client message received: {command}')
        command_list = list(command.split(' '))
        function_name = command_list[0]
        function_arg = command_list[1]
        command_dict = {'translate_word': 'translate_word',
                        'square_int': 'square_int'}

        print('Server running class method (function) with arg as follows: '
              f'{command_dict[function_name]}({function_arg})')
        for key, value in command_dict.items():
            if function_name == key:
                getattr(s, value)(function_arg)

    def square_int(self, arg):
        self.arg = arg
        pickled_obj = pickle.dumps(arg)

    def translate_word(self, arg):
        self.arg = arg
        pickled_obj = pickle.dumps(arg)

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
                    returned_client_message = s.get_client_connection(self.server)
                    s.process_message(s, returned_client_message)

            except socket.error as e:
                print('Client already bound to socket')


def main():
    """Server program main function. Instatiates class object and then calls
       run_server method of the class, which calls get_client_connection class"""
    s = RunServer('127.0.0.1', 9999)
    return_val = s.run_server(s)
    s.process_message(returned_client_message)

if __name__ == "__main__":
    main()
