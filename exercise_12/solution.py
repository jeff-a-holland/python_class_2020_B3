#!/Users/jeff/.pyenv/shims/python

import cmd

class Calculator(cmd.Cmd):
    """Calculator for positive intergers"""
    args_list = []

    def do_add(self, line):
        Calculator.args_list = [int(x) for x in line.split( ) \
                               if x.isnumeric() and x != '0']
        sum = 0
        for value in Calculator.args_list:
            sum += value
        print(sum)

    def do_sub(self, line):
        Calculator.args_list = [int(x) for x in line.split( ) \
                               if x.isnumeric() and x != '0']
        for count, value in enumerate(Calculator.args_list):
            if count == 0:
                difference = Calculator.args_list[0]
            else:
                difference -= value
        print(difference)

    def do_mul(self, line):
        Calculator.args_list = [int(x) for x in line.split( ) \
                               if x.isnumeric() and x != '0']
        product = 1
        for value in Calculator.args_list:
            product *= value
        print(product)

    def do_div(self, line):
        Calculator.args_list = [int(x) for x in line.split( ) \
                               if x.isnumeric() and x != '0']
        divisor = 1
        for value in Calculator.args_list:
            divisor /= value
        print(divisor)

    # Handle using '+' instead of 'add', etc. Also handle using 'quit' instead
    # of 'EOF' to exit. Also check for unsupported command.
    def default(self, line):
        if line[:1] == '+':
            self.do_add(line)
        elif line[:1] == '-':
            self.do_sub(line)
        elif line[:1] == '*':
            self.do_mul(line)
        elif line[:1] == '/':
            self.do_div(line)
        elif line[0:4].lower() == 'quit':
            exit()
        else:
            print('Unsupported command. Please try again.')

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    Calculator().cmdloop()
