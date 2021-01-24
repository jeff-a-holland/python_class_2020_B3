#!/Users/jeff/.pyenv/shims/python

from queue import PriorityQueue
from threading import Thread
import time
import random
import sys

def main():
    """Main functin for Threadify solution"""

    def add(q, x, y, tuple):
        """Add function. Simply return the sumer of values in a tuple passed
        as the argument."""
        sum = 0
        start = time.time()
        for value in tuple:
            sum += value
            time.sleep(random.randint(1, 7))
        stop = time.time()
        elapsed = stop - start
        print(f'  Time spent in add function for Thread-{y} with '
              f'priority {y}: {elapsed}')
        # Put sum of tuple in proper index position based on queue priority
        # value passed in from threadify function (which is the argument 'x')
        print(f'  Putting sum value {sum} in index {x} of result_list for '
              f'Thread-{y}\n  --')
        result_list[x] = sum
        sum = 0
        q.task_done()

    def threadify(func, input_list):
        """Threadify function. Calls the add function x times, where is the
        cardinality of the number of tuples in the list passed as the second
        argument (the function to call being the first argument). Threadify
        will run the add computations in parallel using a PriorityQueue."""

        q = PriorityQueue()
        for index, value in enumerate(input_list, start=1):
            q.put((index, value))
        print('\nPriorityQueue for list of tuples is as follows:')
        for item in q.queue:
            print(f'  {item}')
        print('  ------------')

        for x in range(num_tuples):
            y = x + 1
            tuple_str = q.get()
            tuple_str = tuple_str[1]
            tuple_str = tuple_str[1:]
            tuple_str = tuple_str[:-1]
            tuple_val = tuple(map(int, tuple_str.split(',')))
            worker = Thread(target=add, name=y, args=(q, x, y, tuple_val,))
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
    num_tuples = len(input_list)

    # Set result_list to proper size based on number of threads
    result_list = [0] * num_tuples

    output = threadify(func, input_list)
    print(f'Sum of each tuple from argument list is: {output}')

if __name__ == "__main__":
    main()
