import unittest
from sysadmin import list_all_files
from sysadmin import get_page

class TestListAllFiles(unittest.TestCase):
    def test_does_not_crash_on_empty_path(self):
        actual = [x for x in list_all_files(None)]
        self.assertEqual([], actual)

    def test_inspect_directory_above(self):
        actual = [x for x in list_all_files('../')]
        self.assertGreater(len(actual), 0)

    def test_get_page(self):
        self.assertEqual(True, get_page('https://google.com'))

if __name__ == '__main__':
    unittest.main()
