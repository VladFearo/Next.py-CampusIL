import unittest

def four_dividers(number):
    return list(filter(lambda x: x % 4 == 0, range(1, number)))

class TestFourDividers(unittest.TestCase):

    def test_four_dividers_basic(self):
        self.assertEqual(four_dividers(9), [4, 8])

    def test_four_dividers_with_number_below_four_returns_empty_list(self):
        self.assertEqual(four_dividers(3), [])

if __name__ == '__main__':
    unittest.main()
