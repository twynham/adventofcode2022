import unittest
from filelisting import FileListing


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with open('testinput.txt') as f:
            testData = f.read()
            listing = FileListing(testData)
            self.assertEqual(95437, listing.getfileusage())  # add assertion here


if __name__ == '__main__':
    unittest.main()
