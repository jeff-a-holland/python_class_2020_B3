#!/Users/jeff/.pyenv/shims/python

from queue import PriorityQueue
from threading import Thread

result_list = []

def main():
    """Main function for threadify, which runs a function in parrallel Using
    arguments supplied in a tuple from the command line."""

    #def add(q):
    def add(q, tuple):
        """Add function. Simply return the sumer of values in a tuple passed
        as the argument."""
        sum = 0
        while True:
            tuple = q.get()
            tuple = tuple[1]
            #print(f'tuple is: {tuple}')
            for value in tuple:
                sum += value
            #print(f'sum is: {sum}\n')
            result_list.append(sum)
            q.task_done()
            sum = 0

    def threadify(func, arg_list):
        """Threadify function. Calls the add function x times, where is the
        cardinality of the number of tuples in the list passed as the second
        argument (the function to call being the first argument). Threadify
        will run the add computations in parallel using a PriorityQueue."""

        q = PriorityQueue()
        for index, value in enumerate(arg_list, start=1):
            q.put((index, value))

        num_threads = len(arg_list)
        #print(f'num_threads is: {num_threads}\n')
        for x in range(num_threads):
            #print(f'x is: {x}')
            #print(f'arg_list[x] is: {arg_list[x]}')
            worker = Thread(target=add, args=(q, arg_list[x],))
            worker.setDaemon(True)
            worker.start()

    func_dict = {'add':add}
    arg_list = [(1,2), (3,4), (5,6)]

    threadify(add, arg_list)
    #print(f'result_list is: {result_list}')
    print(result_list)

if __name__ == '__main__':
   main()
