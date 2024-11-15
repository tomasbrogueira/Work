#! /usr/bin/env python3
''' tesstamp for ex15.py '''
import unittest
from ex03 import Data
from ex04 import Relogio
SKIP = False
try :
    import ex15
except ImportError:
    SKIP = True
class TestEx15(unittest.TestCase):
    ''' test class for ex15.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex15.py")
        self.unit = ex15
    def test_stamp(self):
        ''' Test sequence for '.eh_time_stamp()' '''
        stamp = self.unit.TimeStamp(Data(21, 12, 2021), Relogio(12, 21, 59))
        self.assertTrue(self.unit.TimeStamp.eh_time_stamp(stamp))
    def test_nostamp(self):
        ''' Test sequence for 'not .eh_time_stamp()' '''
        stamp = (Data(21, 12, 2021), Relogio(12, 21, 59))
        self.assertFalse(self.unit.TimeStamp.eh_time_stamp(stamp))
    def test_data(self):
        ''' Test sequence for '.data()' '''
        dat = Data(21, 12, 2021)
        rel = Relogio(12, 21, 59)
        stamp = self.unit.TimeStamp(dat, rel)
        self.assertEqual(dat, stamp.data())
    def test_relogio(self):
        ''' Test sequence for '.relogio()' '''
        dat = Data(21, 12, 2021)
        rel = Relogio(12, 21, 59)
        stamp = self.unit.TimeStamp(dat, rel)
        self.assertEqual(rel, stamp.relogio())
    def test_mesmo(self):
        ''' Test sequence for '.mesmo_time_stamp()' '''
        stamp = self.unit.TimeStamp(Data(21, 12, 2021), Relogio(12, 21, 59))
        stamp2 = self.unit.TimeStamp(Data(21, 12, 2021), Relogio(12, 21, 59))
        self.assertTrue(stamp.mesmo_time_stamp(stamp2))
        self.assertTrue(stamp2.mesmo_time_stamp(stamp))
    def test_diff(self):
        ''' Test sequence for 'not .mesmo_time_stamp()' '''
        stamp = self.unit.TimeStamp(Data(21, 12, 2021), Relogio(12, 21, 59))
        stamp2 = self.unit.TimeStamp(Data(21, 12, 2021), Relogio(12, 21, 58))
        self.assertFalse(stamp.mesmo_time_stamp(stamp2))
    def test_antes(self):
        ''' Test sequence for 'not .depois()' '''
        stamp = self.unit.TimeStamp(Data(21, 12, 2021), Relogio(12, 21, 59))
        stamp2 = self.unit.TimeStamp(Data(21, 12, 2021), Relogio(12, 21, 58))
        self.assertFalse(stamp2.depois(stamp))
    def test_depois(self):
        ''' Test sequence for '.depois()' '''
        stamp = self.unit.TimeStamp(Data(21, 12, 2021), Relogio(12, 21, 59))
        stamp2 = self.unit.TimeStamp(Data(21, 12, 2021), Relogio(12, 21, 58))
        self.assertTrue(stamp.depois(stamp2))

if __name__ == '__main__':
    unittest.main()
