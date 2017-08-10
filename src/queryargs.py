from re import compile
from re import findall

import unittest

def parseQueryParams(url):
    regex = compile(r'\w+=\w+&?')
    params = {}
    for pair in regex.findall(url):
        if pair.endswith('&'):
            m = pair[:len(pair)-1]
        else:
            m = pair
        vals = m.split('=')
        lhs = vals[0]
        rhs = vals[1]
        params[lhs] = rhs
    return params

class TestParseQueryParams(unittest.TestCase):
    def test_foo(self):
        result = parseQueryParams('https://example.com?a=foo&cmc=bar')
        self.assertEqual(2, len(result.keys()))
        self.assertEqual('foo', result['a'])
        self.assertEqual('bar', result['cmc'])

if __name__ == '__main__':
    unittest.main()
