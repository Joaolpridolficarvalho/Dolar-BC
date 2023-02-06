import unittest
from src import Dolar_BC

class USD(unittest.TestCase):
    def test_show_value(self):
        self.assertListEqual(Dolar_BC.USD.show_values((Dolar_BC.USD("31/01/2023", "01/02/2023"))), [{'Date': '31/01/2023','Buy': 5.0987, 'Sell': 5.0993},
                                                                                                    {'Date': '01/02/2023', 'Buy': 5.0715, 'Sell': 5.0721}]) #test 001
        self.assertListEqual(Dolar_BC.USD.show_values((Dolar_BC.USD("31/01/2023", "31/01/2023"))), [])  # test 002
        self.assertListEqual(Dolar_BC.USD.show_values((Dolar_BC.USD("31/01/2023", "30/01/2023"))), [])# test 003
        self.assertListEqual(Dolar_BC.USD.show_values((Dolar_BC.USD("31/01/2022", "31/01/2023"))), [])# test 004
        self.assertListEqual(Dolar_BC.USD.show_values((Dolar_BC.USD("aaa", "bbb"))), [])# test 005
        self.assertListEqual(Dolar_BC.USD.show_values((Dolar_BC.USD("31/01/2023", "31/04/2022"))), [])# test 006

    def test_USD2BRL(self):
        self.assertDictEqual(Dolar_BC.USD.USD2BRL((Dolar_BC.USD("31/01/2023", "01/02/2023")), 0.00),{"Value of conversion (buy)": 0.00,
                                                                                                     "Value of conversion (sell)": 0.00})
        self.assertDictEqual(Dolar_BC.USD.USD2BRL((Dolar_BC.USD("31/01/2023", "01/02/2023")), "ssss"),{"Value of conversion (buy)": 0.00,
                                                                                                       "Value of conversion (sell)": 0.00})


if __name__ == '__main__':
    unittest.main()
