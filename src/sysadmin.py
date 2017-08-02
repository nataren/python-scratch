from os import walk
from os.path import abspath
from os.path import join
from os.path import exists
from os.path import isdir
from os.path import isfile
import sys
import requests
import re
from re import compile
from re import finditer
import random

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

regex = compile(r'^(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<userid>[\w-]+)\s+(?P<username>\w+)\s+\[(?P<dt>(\d{1,2})/(\w+)/([\w\s\-:]+))\]\s+"(?P<verb>\w+)\s+(?P<route>[/\w\.]+)\s+(?P<protocol>[\w\/\.]+)"\s+(?P<status>\d{3})\s+(?P<bytecount>\d+)$', re.M)

def parse_ncsa_log(path):
    def parse(text):
        return finditer(regex, text)

    if path is None or not exists(path):
        raise StopIteration

    with open(path, 'r') as f:
        for m in parse(f.read()):
            if m is None:
                yield None
            else:
                yield m.groupdict()
    raise StopIteration

def get_page(url):
    r = requests.get(url)
    return r.status_code == 200

def post_page(url, **kwargs):
    return requests.post(url, **kwargs)

def manipulate_json(url):
    pass

def tpc_server(port):
    pass


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Usage: sysadmin.py PATH')
        sys.exit(1)
    else:
        arg = sys.argv[1]
        for x in list_all_files(arg):
            print(x)
