import unittest
from ex04 import gcd

class TestEx04(unittest.TestCase):
    
    def test_zero_neg(self):
        self.assertEqual(gcd(0,1),0)
        self.assertEqual(gcd(2,0),0)
        self.assertEqual(gcd(0,-1),0)
        self.assertEqual(gcd(1,-1),0)
        self.assertEqual(gcd(-1,3),0)
        self.assertEqual(gcd(0,0),0)
        self.assertEqual(gcd(0,2),0)

    def test_uma_vez(self):
        self.assertEqual(gcd(2,2),2)
        self.assertEqual(gcd(2,4),2)
        self.assertEqual(gcd(4,2),2)
        self.assertEqual(gcd(2,8),2)
    
    def test_str(self):
        self.assertEqual(gcd(1,'a'),ValueError)
        self.assertEqual(gcd('a','a'),ValueError)
        self.assertEqual(gcd('e',2),ValueError)
        self.assertEqual(gcd('c','z'),ValueError)

if __name__ == '__main__':
    unittest.main()