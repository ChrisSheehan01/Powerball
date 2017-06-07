import unittest
import Powerball


class TestForValidNumbers(unittest.TestCase):

    def setUp(self):
        Powerball.nameAndFavNums[:] = []

    def tearDown(self):
        Powerball.nameAndFavNums[:] = []

    def testTrueNum(self):
        Powerball.nameAndFavNums = ['name']
        for trueNum in [1, 69, 34, 11, 46]:
            self.assertEqual(Powerball.valid_num_input(trueNum), True)

    def testFalseNum(self):
        Powerball.nameAndFavNums = ['name']
        for falseNum in [0, 70, 99, -5]:
            self.assertEqual(Powerball.valid_num_input(falseNum), False)

    def testNumsWithArray(self):
        for i in ["a", 2, 3, 4, 5, 6, 7]:
            self.assertEqual(Powerball.valid_num_input(i), True)
            Powerball.nameAndFavNums.append(i)

    def testNumsWithArray2(self):
        for i in ["name", 2, 3, 4, 5, 6]:
            Powerball.nameAndFavNums.append(i)
        self.assertEqual(Powerball.valid_num_input(27), False)

    def testRepeatNums(self):
        for i in ["name", 1, 2, 3, 4]:
            Powerball.nameAndFavNums.append(i)
        for j in [1, 2, 3, 4]:
            self.assertEqual(Powerball.valid_num_input(j), False)
