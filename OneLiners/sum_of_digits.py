import unittest

def sum_of_digits(number):
    return sum(int(n) for n in str(number))


print(sum_of_digits(104))
class TestSumOfDigits(unittest.TestCase):

    def test_sum_of_digits_basic(self):
        self.assertEqual(sum_of_digits(104), 5)

if __name__ == '__main__':
    unittest.main()
