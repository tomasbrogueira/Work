from math import sqrt

def heron(a,b,c):
    if a <= 0 or b <= 0 or c <= 0 or not isinstance(a, int or float) \
                          or not isinstance(b, int or float) or not isinstance(c,int or float):
        raise ValueError('argumentos invalidos')
    
    s = (a+b+c)/2
    
    return sqrt(s*(s-a)*(s-b)*(s-c))

import unittest

class HeronTest(unittest.TestCase):
    def test_default(self):
        self.assertEqual(6,heron(3,4,5))
    
    def test_lados_negativos(self):
        self.assertRaises(ValueError,heron(-1,2,3))
    
    def test_not_num(self):
        self.assertRaises(ValueError,heron(3,'a',1))
    
    def test_neg_and_num(self):
        self.assertRaises(ValueError,heron(1,-2,'b'))

if __name__ == '__main__':
    unittest()