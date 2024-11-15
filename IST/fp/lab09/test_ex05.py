import unittest
from ex05 import noroots

class TestNorootss(unittest.TestCase):

    def test_verdadeiro(self):
        self.assertEqual(noroots(1,1,1),True)
        self.assertEqual(noroots(4,1,1),True)
        self.assertEqual(noroots(1,1,3),True)
        self.assertEqual(noroots(6,5,7),True)
        self.assertEqual(noroots(3,2,1),True)
        self.assertEqual(noroots(3,2,5),True)
        self.assertEqual(noroots(4,5,2),True)
        self.assertEqual(noroots(1,1,2),True)
    
    def test_falsos(self):
        self.assertEqual(noroots(1,3,1),False)
        self.assertEqual(noroots(1,2,1),False)
        self.assertEqual(noroots(2,4,1),False)
        self.assertEqual(noroots(1,5,3),False)
        self.assertEqual(noroots(10,13,2),False)

if __name__ == '__main__':
    unittest.main()