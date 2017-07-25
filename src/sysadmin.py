import os
import sys

def list_all_files(path):
    if path is None:
        raise StopIteration
    absolute_path = os.path.abspath(path)
    if not os.path.exists(absolute_path):
        raise StopIteration
    if os.path.isfile(absolute_path):
        print "`%s` is a file"
        yield path
    if os.path.isdir(absolute_path):
        for root, dirs, files in os.walk(absolute_path):
            print "%s" % root
            for dir in dirs:
                print "\tdir=%s" % dir
                yield dir
            for file in files:
                print "\tfiles=%s" % file
                yield file

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print "Usage: sysadmin.py PATH"
        sys.exit(1)
    else:
        list_all_files(sys.argv[1])
