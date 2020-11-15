#!/Users/jeff/.pyenv/shims/python

from zipfile import ZipFile
import tarfile
import re
import os
import shutil

def tar_to_zip(*inputfiles, **zip_path):
    """Supply valid tarballs as input files to be untar'd and then zipped up.
       Supply a staging directory for the tarballs and zip files. Do not use
       the local directory. Use a new local subdirectory, or  a  new
       subdirectory in /tmp."""

    # Get path to create output zip files in from named kwarg
    for path in zip_path.values():
        zippath = path
        cwd = os.getcwd()
        if str(zippath) == '.' or str(zippath) == cwd or str(zippath) == '/tmp':
            print (f'\nzippath named argument is: {zippath}\n\n  Do not untar and '
                    'zip files to the local directory or /tmp.\n  Use a '
                    'local subdirectory or a subdirectory in /tmp\n\nExiting...\n')
            exit()

        elif str(zippath) == '':
            zippath = '/tmp/zipped'
            print ('\nNo zip_path argument passed.\n'
                      f'Setting zippath named argument to: {zippath}')

        else:
            print (f'\nzippath named argument is: {zippath}')

    # Determine if directory where we'll write zip files to exists.
    # If not, create it and chmod it 777.
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

            # We'll name our zip file based on the root of the tarball name.
            # Parse out the root of the name to "tar_root", truncating .tar or
            # .tar.gz, or .tar.bz2
            file_path_str = str(inputfile)
            path_list = file_path_str.split('/')
            tar_filename = path_list.pop()
            tar_root = re.sub('\\.tar(?:\\.bz2|\\.gz)?', '', tar_filename)

            # Ignore "dot" files, such as "._" created by OSX.
            # Also ignore .tar files for our .zip file, as well as previous
            # .zip files if more than one file was supplied to the function.
            file_full_path_list = []
            files = os.listdir(zippath)
            for file in files:
                if not file.startswith('.') and not file.endswith('.tar') and\
                   not file.endswith('.zip'):
                    file_full_path_list.append(str(zippath) + '/' + file)

            # Build list of file untar'd that we'll zip up. Then create the
            # .zip that contains all the same files from the tarball.
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

            # CLean up the directory where we untar'd the tarball, except
            # for the .zip file we just created. Make sure to delete both
            # files and any directories recursively.
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
#tar_to_zip('test.tar', 'test2.tar', 'test3.tar', zippath='/tmp/test')
#tar_to_zip('test.tar', 'test2.tar', 'test3.tar', 'test4.tar.bz2', zippath='/tmp/test')
#tar_to_zip('test.tar', 'test2.tar', 'test3.tar', 'test4.tar.bz2', 'test5.tar.gz', zippath='.')
tar_to_zip('test.tar', 'test2.tar', 'test3.tar', 'test4.tar.bz2', 'test5.tar.gz', zippath='')
#tar_to_zip('test.tar', 'test2.tar', 'test3.tar', 'test4.tar.bz2', 'test5.tar.gz', zippath='/tmp')
#tar_to_zip('test.tar', 'test2.tar', 'test3.tar', 'test4.tar.bz2', 'test5.tar.gz', zippath='/tmp/test')
