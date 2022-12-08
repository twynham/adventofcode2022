import unittest
from forest import Trees


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with open('testinput.txt') as f:
            testData = f.read()
            trees = Trees(testData)
            self.assertEqual(21, trees.count())  # add assertion here


if __name__ == '__main__':
    unittest.main()
