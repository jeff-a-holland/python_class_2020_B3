#!/Users/jeff/.pyenv/shims/python

from pathlib import Path
import os

class TempFile(object):
    def __init__(self, f, mode):
        self.f = f
        self.mode = mode
        fh = open(f, mode)

    def write(self, data):
        self.data = data
        TempFile.fh.write(data)

    def __del__(self):
        print('calling delete method')
        Path(self.f).unlink(missing_ok=True)

tf = TempFile('./testfile.txt', 'w')
write_file_result = tf.write('testing writing data to file\n')
os.system('cat ./testfile2.txt')
