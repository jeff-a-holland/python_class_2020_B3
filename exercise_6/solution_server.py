#!/Users/jeff/.pyenv/shims/python

import socket
import re
import pickle

class RunServer(object):
    """RunServer Class"""
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def get_client_connection(self, s, server):
        """RunServer get_client_connection method. Prints out the client
           command if it was valid, otherwise print non-fatal error to STDOUT."""
        self.s = s
        self.server = server
        try:
            socket_object, client_ip = server.accept()
            with socket_object:
                while True:
                    data = socket_object.recv(1024)
                    client_message = (str(data.decode('utf-8')))
                    client_message_lowercase = (str.lower(data.decode('utf-8')))
                    if data:
                        if client_message_lowercase == 'bye':
                            print(client_message,'\n')
                            socket_object.sendall(data)
                            socket_object.close()
                            exit()

                        else:
                            pickle = s.process_message(s, client_message)
                            socket_object.sendall(pickle)

                    else:
                        break

        except socket.error as e:
            raise SystemExit(f'Error getting client connection: {e}')
        return client_message_lowercase

    def process_message(self, s, command):
        """process_message method. Takes client message with the name of the
        function to run and looks up that function name in a dict along with
        the argument(s) supplied and calls the appropriate method based on the
        function name"""
        self.command = command
        self.s = s
        print(f'Client message received:\n   {command}')
        command_list = list(command.split(' '))
        function_name = command_list.pop(0)
        function_arg = command_list
        command_dict = {'reverse_words': 'reverse_words',
                        'square_int': 'square_int'}

        print('\nServer calling class method (function) with arg as follows:\n'
              f'   {command_dict[function_name]}({function_arg})')
        for key, value in command_dict.items():
            if function_name == key:
                pickled_obj = getattr(s, value)(function_arg)
                return pickled_obj

    def square_int(self, arg):
        """square_int method. Squares the int supplied and returns a pickled
        dict to the client with both the int that was squared and the squared
        value of the int."""
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

    def reverse_words(self, arg):
        """reverse_words method. Reverses the word string and returns a pickled
        list to the client."""
        self.arg = arg
        arg.reverse()
        print(f'\nReversed list object is:\n   {arg}',
               'and is of type:', type(arg))
        pickled_obj = pickle.dumps(arg)
        print(f'\nPickled object is:\n   {pickled_obj}',
               '\n\nSending pickled object back to the client now...\n\n'
               '######################################################\n')
        return pickled_obj

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
                        print('  Now accepting client messages!!\n'
                              '###################################'
                              '###################\n')
                        mssg_flag = True
                    s.get_client_connection(s, self.server)

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
