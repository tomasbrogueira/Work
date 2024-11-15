def trapz(x1,y1,x2,y2):
    if x2 <= x1 or y1 < 0 or y2 < 0:
        raise ValueError('argumentos inválidos')
    return (y1+y2)*(x2-x1)/2

import unittest

class TestTrapz(unittest.TestCase):
    def default(self):
        self.assertEqual(9,trapz(1,2,4,3))
    
    def ordenadas_negativas(self):
        self.assertRaises(ValueError,trapz(1,-1,2,3))
    
    def abcissas_trocadas(self):
        self.assertRaises(ValueError,trapz(2,4,1,2))
    
    def absissas_ordenadas(self):
        self.assertRaises(ValueError,trapz(4,1,2,-3))

if __name__ == '__main__':
    unittest()


def dotproduct(x1,y1,x2,y2):
    return x1*x2+y1*y2

import unittest

class TestDotproduct(unittest.TestCase):
    def default(self):
        self.assertEqual(11,dotproduct(1,2,3,4))
    
    def abcissas_trocadas(self):
        self.assertEqual(11,dotproduct(3,4,1,2))

if __name__ == '__main__':
    unittest()

#make a function that returns the area of a triangle
def area(x1,y1,x2,y2,x3,y3):
    return abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)

#make a hash function that returns the hash of a string
def hash(s):
    h = 0
    for i in range(len(s)):
        h = h + ord(s[i])*(31**(len(s)-i-1))
    return h

