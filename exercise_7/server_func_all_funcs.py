#!/Users/jeff/.pyenv/shims/python
def reverse_words(arg):
    arg.reverse()
    print(arg)
reverse_words(arg)

def square_int(arg):
    arg = int(arg[0])
    arg_squared = arg * arg
    arg_dict = {arg: arg_squared}
    print(arg_dict)
square_int(arg)
