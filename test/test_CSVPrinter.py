import unittest

from ss2022.CSVPrinter import CSVPrinter


class TestCSVPrinter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    def test_read(self):
        l = self.printer.read()
        self.assertEqual(2, len(l))
        print(1)


    def test_read(self):
        print(2)

    def tearDown(self) :
        print("tearDown")
