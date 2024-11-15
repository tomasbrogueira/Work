import unittest
from ex02 import binary

class TestEx02(unittest.TestCase):

    def test_binary_int_positive(self):
        self.assertEqual(binary(2),0)
    
    def test_binary_int_negative(self):
        self.assertEqual(binary(-5),1)

    def test_binary_int_p_less(self):
        self.assertEqual(binary(0),1)

    def test_binary_not_int(self):
        self.assertEqual(binary(0.5),0)
    
    def test_binary_not_num(self):
        self.assertEqual(binary('a'),0)

if __name__ == '__main__':
    unittest.main()
