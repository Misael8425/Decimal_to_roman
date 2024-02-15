import unittest
from Decimal_to_roman import Decimal_to_roman

class TestDecimalToRoman(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(Decimal_to_roman(1), 'I')
        self.assertEqual(Decimal_to_roman(5), 'V')
    
    def test_multiple_digits(self):
        self.assertEqual(Decimal_to_roman(10), 'X')
        self.assertEqual(Decimal_to_roman(50), 'L')
    
    def test_subtractive_notation(self):
        self.assertEqual(Decimal_to_roman(4), 'IV')
        self.assertEqual(Decimal_to_roman(9), 'IX')
    
    def test_large_numbers(self):
        self.assertEqual(Decimal_to_roman(100), 'C')
        self.assertEqual(Decimal_to_roman(500), 'D')

    def test_boundary_values(self):
        self.assertEqual(Decimal_to_roman(3999), 'MMMCMXCIX')
        self.assertEqual(Decimal_to_roman(1), 'I')
        self.assertEqual(Decimal_to_roman(3998), 'MMMCMXCVIII')
        self.assertEqual(Decimal_to_roman(3997), 'MMMCMXCVII')
        self.assertEqual(Decimal_to_roman(3996), 'MMMCMXCVI')

if __name__ == '__main__':
    unittest.main()
