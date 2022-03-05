import unittest

from DataStructures.Tasks.balance_checker import balance_check


class BalanceCheckTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(balance_check('{{([][])}()}'), True)

    def test_2(self):
        self.assertEqual(balance_check('{{([][])}()}'), True)

    def test_3(self):
        self.assertEqual(balance_check('{{([][])}()}('), False)

    def test_4(self):
        self.assertEqual(balance_check('{{([][])}()}('), False)


if __name__ == '__main__':
    unittest.main()
