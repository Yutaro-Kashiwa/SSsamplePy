import unittest
from ss2022.CSVPrinter import CSVPrinter


class TestCSVPrinter(unittest.TestCase):
    def setUp(self):
        self.printer = CSVPrinter("sample.csv")

    def test_read(self):
        l = self.printer.read()
        self.assertEqual(2, len(l))

