import unittest
from crane import Exercise


with open('testinput.txt') as f:
    testData = f.read()

class MyTestCase(unittest.TestCase):
    def test_processor(self):
        self.assertEqual("CMZ", Exercise.processFile(testData))  # add assertion here


if __name__ == '__main__':
    unittest.main()
