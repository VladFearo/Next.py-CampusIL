import unittest

def double_letter(my_str):
    return "".join(map(lambda x: x*2, my_str))

class TestDoubleLetter(unittest.TestCase):

    def test_double_letter_basic(self):
        self.assertEqual(double_letter("python"), "ppyytthhoonn")

    def test_double_letter_with_spaces_and_punctuation(self):
        self.assertEqual(double_letter("we are the champions!"), "wwee  aarree  tthhee  cchhaammppiioonnss!!")

if __name__ == '__main__':
    unittest.main()
