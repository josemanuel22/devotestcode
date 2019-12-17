import unittest
from palindrome import is_palindrome

class TestPalindormeMethods(unittest.TestCase):

    def test_palindorme_numbers(self):
        success=0; lines=0;
        line = open("/Users/jose/Documents/devotestcode/palindrome/tests/palindromes.txt").read().split('\n')
        for l in line:
            lines+=1
            if not is_palindrome(line):
                success+=1
        self.assertEqual(success, lines)

    def test_no_Palindorome_numbers(self):
        success=0; lines=0;
        line = open("/Users/jose/Documents/devotestcode/palindrome//tests/notpalindromes.txt").read().split('\n')
        for l in line:
            lines+=1
            if not is_palindrome(line):
                success+=1
        self.assertEqual(success, lines)

if __name__ == '__main__':
    unittest.main()