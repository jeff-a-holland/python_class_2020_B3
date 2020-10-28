import pickle
import csv

class Serializable():
    def dump(self, filename):
        # convert self object to a dict using vars method
        book_dict = vars(self)
        with open(filename, 'wb') as fh:
            pickle.dump(book_dict, fh)

    def load(self, filename):
        with open(filename, 'rb') as fh:
            file_data_dict = pickle.load(fh)
            # Use setattr to set the keys as attributes of the class
            for key in file_data_dict:
                setattr(self, key, file_data_dict[key])
            return(self)

class CSVMixin():
    def dump(self, filename):
        # convert self object to a dict using vars method
        book_dict = vars(self)
        with open(filename, 'w') as fh:
            file_writer = csv.writer(fh, delimiter=',')
            header = ','.join(book_dict.keys())
            # cast price as a str so we can join with other strings
            data = ','.join(str(value) for value in book_dict.values())
            file_writer.writerow(header)
            file_writer.writerow(data)

    def load(self, filename):
        with open(filename, 'r') as fh:
            file_reader = csv.reader(fh, delimiter=',')
            # declare list for storing list of lists
            file_data_lists = []
            for row in file_reader:
                # add row to file_data_lists
                file_data_lists.append(row)
            # break out lists for header and values
            values_list = file_data_lists.pop()
            header_list = file_data_lists.pop()
            for key in header_list:
                # Use setattr to set the keys as attributes of the class
                # Get first element of header_list using slicing
                setattr(self, key, header_list[1:])
            return(self)


class Book(Serializable):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

b = Book("Practice Makes Python", "Reuven Lerner", 39)
b.dump('book.data')      # book is now stored on disk, in pickle format

b2 = Book('blah title', 'blah author', 100)
b2.load('book.data')     # title, author, and price now reflect disk file

class Book(CSVMixin, Serializable):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

b = Book("Practice Makes Python", "Reuven Lerner", 39)
b.dump('book.csv')      # book is now stored on disk, in CSV format

b2 = Book('blah title', 'blah author', 100)
b2.load('book.csv')     # title, author, and price now reflect disk file
