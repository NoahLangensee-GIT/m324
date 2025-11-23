import unittest

from src.house import House

from io import StringIO

import sys
 
 
class TestHouse(unittest.TestCase):
 
    def test_create(self):

        house = House()

        self.assertIsInstance(house, House)
 
    def test_set_name_valid(self):

        house = House()

        house.set_name("MyHouse")

        self.assertEqual(house.name, "MyHouse")
 
    def test_set_name_invalid_type(self):

        house = House()

        with self.assertRaises(Exception):

            house.set_name(123)  # kein String
 
    def test_get_name_output(self):

        house = House()

        house.set_name("DreamHouse")
 
        captured = StringIO()

        sys.stdout = captured   # print-Ausgabe umleiten
 
        house.get_name()
 
        sys.stdout = sys.__stdout__
 
        self.assertEqual(captured.getvalue().strip(), "DreamHouse")
 
if __name__ == '__main__':

    unittest.main()

 
