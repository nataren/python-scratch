from os import path
from os import walk
from os.path import abspath
from os.path import join
from os.path import exists
from os.path import isdir
from os.path import isfile
import sys

def list_all_files(path):
    if path is None:
        raise StopIteration
    absolute_path = abspath(path)
    if not exists(absolute_path):
        raise StopIteration
    if isfile(absolute_path):
        yield absolute_path
    if isdir(absolute_path):
        for root, dirs, files in walk(absolute_path):
            for dir in dirs:
                yield join(root, dir)
            for file in files:
                yield join(root, file)
    raise StopIteration

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print 'Usage: sysadmin.py PATH'
        sys.exit(1)
    else:
        arg = sys.argv[1]
        for x in list_all_files(arg):
            print x
