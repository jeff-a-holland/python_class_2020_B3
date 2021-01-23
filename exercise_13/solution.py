#!/Users/jeff/.pyenv/shims/python

from queue import PriorityQueue
from threading import Thread

result_list = []

def main():
    """Main function for threadify, which runs a function in parrallel Using
    arguments supplied in a tuple from the command line."""

    #def add(q):
    def add(tuple):
        """Add function. Simply return the sumer of values in a tuple passed
        as the argument."""
        sum = 0
        #while True:
            #tuple = q.get()
        for value in tuple:
            sum += value
        print(f'sum is: {sum}\n')
        result_list.append(sum)
            #q.task_done()

    def threadify(func, arg_list):
        """Threadify function. Calls the add function x times, where is the
        cardinality of the number of tuples in the list passed as the second
        argument (the function to call being the first argument). Threadify
        will run the add computations in parallel using a PriorityQueue."""

        num_threads = len(arg_list)
        print(F'num_threads is: {num_threads}\n')
        for x in range(num_threads):
            print(f'x is: {x}')
            print(f'arg_list[x] is: {arg_list[x]}')
            worker = Thread(target=add, args=(arg_list[x],))
            worker.setDaemon(True)
            worker.start()

        # result_list = []
        # for tuple in arg_list:
        #     result = func_dict.get(func)(tuple)
        #     result_list.append(result)
        # print(f'  Results from threadify function was: {result_list}\n')
        # print(result_list)

    func_dict = {'add':add}
    arg_list = [(1,2), (3,4), (5,6)]

    q = PriorityQueue()
    for index, value in enumerate(arg_list, start=1):
        q.put((index, value))

    threadify(add, arg_list)
    print(f'result_list is: {result_list}')

if __name__ == '__main__':
   main()
