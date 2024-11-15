import unittest
from ex03 import divisores

class TestEx03(unittest.TestCase):

    def test_str(self):
        self.assertEqual(divisores('a'),0)

    def test_not_int(self):
        self.assertEqual(divisores(3.5),-1)
    
    def test_posit_zero_div(self):
        self.assertEqual(divisores(3),0)
    
    def test_neg_zero_div(self):
        self.assertEqual(divisores(-1),0)
    
    def test_posit_2_div(self):
        self.assertEqual(divisores(12),2)
    
    def test_posit_2_div(self):
        self.assertEqual(divisores(-8),2)


if __name__ == '__main__':
    unittest.main()