import unittest
import cleanup


with open('testinput.txt') as f:
    testData = f.read()


class MyTestCase(unittest.TestCase):
    def test_validresult(self):
        self.assertEqual(2, cleanup.process(testData))  # add assertion here

    def test_validresult2(self):
        self.assertEqual(4, cleanup.processoverlap(testData))  # add assertion here



if __name__ == '__main__':
    unittest.main()
