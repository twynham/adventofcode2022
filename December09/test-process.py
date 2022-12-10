import unittest
from process import Rope

class MyTestCase(unittest.TestCase):
    def test_something(self):
        with open('testdata.txt') as f:
            prodData = f.read()
            rope = Rope(prodData)

        self.assertEqual(13, rope.process())  # add assertion here


if __name__ == '__main__':
    unittest.main()
