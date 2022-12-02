import unittest
import calories


with open('testinput.txt') as f:
    testData = f.read()


class MyTestCase(unittest.TestCase):
    def test_output(self):
        self.assertEqual(calories.count(testData, 1), 24000)


if __name__ == '__main__':
    unittest.main()
