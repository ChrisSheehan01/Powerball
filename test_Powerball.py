import unittest
import Powerball

class TestForValidNumbers(unittest.TestCase):

    def setUp(self):
        Powerball.nameAndFavNums[:] = []

    def tearDown(self):
        Powerball.nameAndFavNums[:] = []

    def testTrueNum(self):
        for trueNum in [1, 69, 34, 11, 46]:
            self.assertEqual(Powerball.checkIfValidNum(trueNum), True)

    def testFalseNum(self):
        for falseNum in [0, 70, 99, -5]:
            self.assertEqual(Powerball.checkIfValidNum(falseNum), False)

    def testNumsWithArray(self):
        for i in [1,2,3,4,5,6,7]:
            self.assertEqual(Powerball.checkIfValidNum(i), True)
            Powerball.nameAndFavNums.append(i)

    def testNumsWithArray2(self):
        for i in [1,2,3,4,5,6]:
            Powerball.nameAndFavNums.append(i)
        self.assertEqual(Powerball.checkIfValidNum(27), False)