import unittest
from AddHexNumber import Node, HexNumber

class TestHexNumber(unittest.TestCase):
    def testStr(self):
        self.assertEqual(str(HexNumber('F')), 'F')
        self.assertEqual(str(HexNumber('10')), '10')
        self.assertEqual(str(HexNumber('A31')), 'A31')
        self.assertEqual(str(HexNumber('0')), '0')
        self.assertEqual(str(HexNumber('1')), '1')
        self.assertEqual(str(HexNumber('A0')), 'A0')

    def testAdd(self):
        self.assertEqual(str(HexNumber('31F').add(HexNumber('13'))), '332')
        self.assertEqual(str(HexNumber('100').add(HexNumber('21'))), '121')
        self.assertEqual(str(HexNumber('AAA').add(HexNumber('FFF'))), '1AA9')
        self.assertEqual(str(HexNumber('0').add(HexNumber('0'))), '0')
        self.assertEqual(str(HexNumber('332').add(HexNumber('0'))), '332')
        self.assertEqual(str(HexNumber('1').add(HexNumber('9'))), 'A')