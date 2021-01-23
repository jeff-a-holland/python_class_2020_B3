#!/Users/jeff/.pyenv/shims/python

from queue import PriorityQueue
from threading import Thread
import sys

result_list = []

def add(tuple):
    """Add function. Simply return the sumer of values in a tuple passed
    as the argument."""
    sum = 0
    #print(f'tuple is: {tuple}')
    for value in tuple:
        print(type(value))
        print(value)
        sum += value
    #print(f'sum is: {sum}\n')
    result_list.append(sum)
    sum = 0
    q.task_done()

def threadify(func, input_list):
    """Threadify function. Calls the add function x times, where is the
    cardinality of the number of tuples in the list passed as the second
    argument (the function to call being the first argument). Threadify
    will run the add computations in parallel using a PriorityQueue."""

    print(f'func is: {func}')
    func_dict = {'func': func}
    print(func_dict)
    # q = PriorityQueue()
    # for index, value in enumerate(input_list, start=1):
    #     q.put((index, value))

    num_threads = len(input_list)
    print(f'num_threads is: {num_threads}\n')
    for x in range(num_threads):
        print(f'x is: {x}')
        tuple_str = q.get()
        tuple_str = tuple_str[1]
        tuple_str = tuple_str[1:]
        tuple_str = tuple_str[:-1]
        tuple_val = tuple(map(int, tuple_str.split(',')))
        #print(type(tuple_val))
        #print(f'tuple here is: {tuple_val}')
        print(func_dict.get(func))
        worker = Thread(target=add, args=(tuple_val,))
        #worker = Thread(target=func_dict.get(func), args=(tuple_val,))
        worker.setDaemon(True)
        worker.start()
    q.join()
    return result_list

#arg_list = [(1,2), (3,4), (5,6)]
argv_list = sys.argv
func = argv_list[1]
input_list = argv_list[2]
input_list = input_list[1:]
input_list = input_list[:-1]
#print(input_list)
input_list = input_list.split(', ')
#print(type(input_list))
#print(input_list)

q = PriorityQueue()
for index, value in enumerate(input_list, start=1):
    q.put((index, value))

output = threadify(func, input_list)
print(output)
#print(result_list)
