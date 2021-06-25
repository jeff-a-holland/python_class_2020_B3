#!/Users/jeff/.pyenv/shims/python

from solution import TempFile
from os.path import isfile, exists


def test_simple():
    filename = '/tmp/myfile.txt'
    assert not exists(filename)
    f = TempFile(filename, 'w')
    f.write('abc\n')
    f.close()
    assert exists(filename)
    del(f)
    assert not exists(filename)


def test_methods():
    filename = '/tmp/myfile.txt'
    assert not exists(filename)
    f = TempFile(filename, 'w+')
    for one_word in 'abc def ghi jkl'.split():
        f.write(f'{one_word}\n')

    assert f.tell() == 16
    f.seek(3)
    assert f.read(4) == '\ndef'

    f.close()
    assert exists(filename)
    del(f)
    assert not exists(filename)


def test_in_with():
    filename = '/tmp/myfile.txt'
    assert not exists(filename)
    with TempFile(filename, 'w') as f:
        f.write('abc\n')

    assert exists(filename)
    del(f)
    assert not exists(filename)


def test_additional_reference():
    filename = '/tmp/myfile.txt'
    assert not exists(filename)
    with TempFile(filename, 'w') as f:
        f.write('abc\n')

    f2 = f
    assert exists(filename)
    del(f)
    assert exists(filename)
    del(f2)
    assert not exists(filename)
