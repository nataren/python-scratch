from os import walk
from os.path import abspath
from os.path import join
from os.path import exists
from os.path import isdir
from os.path import isfile
import sys
import requests

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

# Sample: 127.0.0.1 user-identifier frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326

match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w+)\s+(\w+)\s+\[(\d{1,2})/(\w+)/([\w\s\-:]+)\]\s+"(\w+)\s+([/\w\.]+)\s+([\w/\.]+)"\s+(\d{3,3})\s+(\d+)', '192.168.0.2 userid frank [12/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326')

def parse_ncsa_log(path):
    regex = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w+)\s+(\w+)\s+\[(\d{1,2})/(\w+)/([\w\s\-:]+)\]\s+"(\w+)\s+([/\w\.]+)\s+([\w/\.]+)"\s+(\d{3,3})\s+(\d+)', '192.168.0.2 userid frank [12/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326'

    def parse(text):
        m = search(regex, text)
        if m is not None:
            m.groups()
        return None

    if path is None or not exists(path):
        raise StopIteration

    with open(path, 'r') as f:
        for line in f:
            yield parse(line)

    raise StopIteration

def get_page(url):
    r = requests.get(url)
    return r.status_code == 200

def post_page(url):
    pass

def manipulate_json(url):
    pass

def tpc_server(port):
    pass


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print 'Usage: sysadmin.py PATH'
        sys.exit(1)
    else:
        arg = sys.argv[1]
        for x in list_all_files(arg):
            print x
