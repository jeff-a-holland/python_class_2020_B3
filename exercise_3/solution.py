#!/Users/jeff/.pyenv/shims/python

from zipfile import ZipFile
import tarfile
import re
import os

def tar_to_zip(*args, **zippath):
    zippath = './'
    extraction_dir = '/tmp'
    tmp_dir_file_before = os.listdir(extraction_dir)
    print(f'before: {tmp_dir_file_before}')

    for arg in args:
        if arg.startswith('zippath'):
            zippath = re.sub('^.*?=', '', arg) + '/'
            print (f'\nzippath is: {zippath}')

        elif tarfile.is_tarfile(arg):
            print (f'\n{arg} is a tarfile. Proceeding to untar it...')
            tf = tarfile.open(arg, 'r')
            tf.extractall(extraction_dir)

        else:
            print(f'\nERROR. {arg} is NOT a tarfile. Skipping this file...')

    tmp_dir_file_after = os.listdir(extraction_dir)
    print(f'after: {tmp_dir_file_after}')
    for file in tmp_dir_file_after:
        if file not in tmp_dir_file_before and not file.startswith('._'):
            print(f'file that should be zipped: {file}')
            file2 = re.sub('\..*', '', file)
            zipped_file = zippath + file2 + '.zip'
            print(f'zipped_file path/name is: {zipped_file}')
            with ZipFile(zipped_file, 'w') as zipped:
                zipped.write(zipped_file)
                untard_file1 = extraction_dir + '/' + file
                untard_file2 = extraction_dir + '/' + '._' + file
                os.remove(untard_file1)
                os.remove(untard_file2)


#tar_to_zip('text.tar', 'tard_and_zipd.tar', 'tard_zipd_compressed.tar.gz')
#tar_to_zip('text.tar', 'tard_and_zipd.tar', 'tard_zipd_compressed.tar.gz', 'zippath=/tmp')
