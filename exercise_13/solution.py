#!/Users/jeff/.pyenv/shims/python

from queue import PriorityQueue
from threading import Thread
import time
import random
import sys

result_list = []

def main():
    """Main functin for Threadify solution"""

    def add(x, tuple):
        """Add function. Simply return the sumer of values in a tuple passed
        as the argument."""
        sum = 0
        start = time.time()
        for value in tuple:
            sum += value
        result_list.append(sum)
        sum = 0
        time.sleep(random.randint(1, 7))
        stop = time.time()
        elapsed = stop - start
        print(f'  Time spent in add function for Thread-{x} with priority {x}: {elapsed}')
        q.task_done()

    def threadify(func, input_list):
        """Threadify function. Calls the add function x times, where is the
        cardinality of the number of tuples in the list passed as the second
        argument (the function to call being the first argument). Threadify
        will run the add computations in parallel using a PriorityQueue."""

        num_threads = len(input_list)
        for x in range(num_threads):
            y = x + 1
            tuple_str = q.get()
            tuple_str = tuple_str[1]
            tuple_str = tuple_str[1:]
            tuple_str = tuple_str[:-1]
            tuple_val = tuple(map(int, tuple_str.split(',')))
            worker = Thread(target=add, name=y, args=(y, tuple_val,))
            worker.setDaemon(True)
            worker.start()
        q.join()
        return result_list

    argv_list = sys.argv
    func = argv_list[1]
    input_list = argv_list[2]
    input_list = input_list[1:]
    input_list = input_list[:-1]
    input_list = input_list.split(', ')

    q = PriorityQueue()
    for index, value in enumerate(input_list, start=1):
        q.put((index, value))
    print('\nPriorityQueue for list of tuples is as follows:')
    for item in q.queue:
        print(f'  {item}')
    print('  ---')

    output = threadify(func, input_list)
    print(f'  ---\n  Sum of each tuple from argument list is: {output}\n')

if __name__ == "__main__":
    main()
