import unittest
from ex01 import nand
class TestEx01(unittest.TestCase):
    def test_bool_a_num(self):
        self.assertEqual(nand(3,False),False)
    def test_bool_a_str(self):
        self.assertEqual(nand('lol',False),False)
    def test_bool_b_num(self):
        self.assertEqual(nand(True,1),False)
    def test_bool_b_str(self):
        self.assertEqual(nand(True,'comunismo'),False)
    def test_both_bool_1(self):
        self.assertEqual(nand(True,False),True)
    def test_both_bool_2(self):
        self.assertEqual(nand(False,True),True)
    def test_both_bool_3(self):
        self.assertEqual(nand(True,True),False)
    def test_both_bool_4(self):
        self.assertEqual(nand(False,False),True)
    def test_none_bool(self):
        self.assertEqual(nand(1,'t'),False)

if __name__ == "__main__" :
    unittest.main()
    

    