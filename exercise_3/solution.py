#!/Users/jeff/.pyenv/shims/python

from zipfile import ZipFile
import tarfile
import re
import os

def tar_to_zip(*inputfiles, **zip_path):

    for path in zip_path.values():
        zippath = path
        print (f'\nzippath is: {zippath}')

    file_status = str(os.path.exists(zippath))
    if file_status == 'False':
        print('Creating dir')
        os.mkdir(str(zippath), 0o666)
    else:
        print('Dir already exists')

    for inputfile in inputfiles:
        if tarfile.is_tarfile(inputfile):
            print (f'\n{inputfile} is a tarfile. Proceeding to untar it...')
            tf = tarfile.open(inputfile, 'r')
            tf.extractall('./')

            file_path_str = str(inputfile)
            path_list = file_path_str.split('/')
            tar_filename = path_list.pop()
            print(f'\ntar\'d filename is: {tar_filename}')
            tar_root = re.sub('\\.tar', '', tar_filename)
            print(f'\nfilename after removing extension is: {tar_root}')

            file_full_path_list = []
            files = os.listdir(zippath)
            print(files)

            for file in files:
                if not file.startswith('.') and not file.endswith('.tar'):
                    print (file)
                    file_full_path_list.append(str(zippath) + '/' + file)
            print(f'file_full_path_list is: {file_full_path_list}')

            untard_file_list = []
            for file in file_full_path_list:
                if not file.endswith('.tar'):
                    untard_file_list.append(file)
            print(f'untard_file_list: {untard_file_list}')
            path_to_write_to = str(zippath) + '/' + tar_root + '.zip'
            print (f'path_to_write_to is: {path_to_write_to}')
            with ZipFile(f'{path_to_write_to}', 'w') as zipped:
                for file in untard_file_list:
                    print(f'file that should be zipped: {file}')
                    filename = file
                    filename = re.sub('^.*/', '', filename)
                    print (f'filename is: {filename}')
                    zipped.write(file, filename)

        else:
            print(f'\nERROR. {inputfile} is NOT a tarfile. Skipping this file...')

#tar_to_zip('test.tar', zippath='./temp')
