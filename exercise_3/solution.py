#!/Users/jeff/.pyenv/shims/python

from zipfile import ZipFile
import tarfile
import re
import os
import shutil

def tar_to_zip(*inputfiles, **zip_path):

    for path in zip_path.values():
        zippath = path
        print (f'\nzippath named argument is: {zippath}')

    file_status = str(os.path.exists(zippath))
    if file_status == 'False':
        print(f'\n  {zippath} does not exist. Creating directory...')
        os.mkdir(str(zippath))
        os.chmod(str(zippath), 0o777)
    else:
        print(f'\n  {zippath} directory already exists. Continuing...')

    for inputfile in inputfiles:
        if tarfile.is_tarfile(inputfile):
            print (f'\n      {inputfile} is a tarfile. Proceeding to untar it...')
            tf = tarfile.open(inputfile, 'r')
            tf.extractall(zippath)

            file_path_str = str(inputfile)
            path_list = file_path_str.split('/')
            tar_filename = path_list.pop()
            tar_root = re.sub('\\.tar', '', tar_filename)

            file_full_path_list = []
            files = os.listdir(zippath)

            for file in files:
                if not file.startswith('.') and not file.endswith('.tar') and\
                   not file.endswith('.zip'):
                    file_full_path_list.append(str(zippath) + '/' + file)

            untard_file_list = []
            for file in file_full_path_list:
                if not file.endswith('.tar'):
                    untard_file_list.append(file)
            path_to_write_to = str(zippath) + '/' + tar_root + '.zip'
            with ZipFile(f'{path_to_write_to}', 'w') as zipped:
                for file in untard_file_list:
                    filename = file
                    filename = re.sub('^.*/', '', filename)
                    zipped.write(file, filename)

            files = os.listdir(zippath)
            for file in files:
                if not file.endswith('.zip'):
                    filepath = str(zippath) + '/' + file
                    if os.path.isdir(filepath):
                        shutil.rmtree(str(filepath))
                    elif os.path.isfile(filepath):
                        os.remove(filepath)

        else:
            print(f'\n      ERROR. {inputfile} is NOT a tarfile. Skipping this file...')

    print (f'\nDone. See your zip files in the directory: {zippath}\n')

#tar_to_zip('test.tar', zippath='./temp')
#tar_to_zip('test.tar', 'test2.tar', zippath='./temp')
#tar_to_zip('test.tar', 'test2.tar', zippath='/tmp/test')
tar_to_zip('test.tar', 'test2.tar', 'test3.tar', zippath='/tmp/test')
