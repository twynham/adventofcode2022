import unittest
import calories


with open('testinput.txt') as f:
    testData = f.read()


class MyTestCase(unittest.TestCase):
    def test_max_output(self):
        self.assertEqual(24000, calories.count(testData, 0))

    def test_min_output(self):
        self.assertEqual(6000, calories.count(testData, 3))


if __name__ == '__main__':
    unittest.main()
