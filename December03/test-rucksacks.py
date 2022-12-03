import unittest
import rucksacks


with open('testinput.txt') as f:
    testData = f.read()


class MyTestCase(unittest.TestCase):
    def test_validresult(self):
        self.assertEqual(157, rucksacks.process_rucksack(testData))  # add assertion here

    def test_validgrouping(self):
        self.assertEqual(70, rucksacks.process_groupings(testData))  # add assertion here



if __name__ == '__main__':
    unittest.main()
