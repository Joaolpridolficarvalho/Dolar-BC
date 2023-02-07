import unittest
from src import Dolar_BC

class USD(unittest.TestCase):
    def test_show_value(self):
        self.assertListEqual(Dolar_BC.USD.show_values((Dolar_BC.USD("31/01/2023", "01/02/2023"))), [{'Date': '31/01/2023','Buy': 5.0987, 'Sell': 5.0993},
                                                                                                    {'Date': '01/02/2023', 'Buy': 5.0715, 'Sell': 5.0721}])
        self.assertListEqual(Dolar_BC.USD.show_values((Dolar_BC.USD("31/01/2023", "31/01/2023"))), [])
        self.assertListEqual(Dolar_BC.USD.show_values((Dolar_BC.USD("31/01/2023", "30/01/2023"))), [])
        self.assertListEqual(Dolar_BC.USD.show_values((Dolar_BC.USD("31/01/2022", "31/01/2023"))), [])
        self.assertIn({'Date': '29/07/2022', 'Buy': 5.1878, 'Sell': 5.1884}, Dolar_BC.USD.show_values((Dolar_BC.USD("30/01/2022", "30/07/2022"))))
        self.assertListEqual(Dolar_BC.USD.show_values((Dolar_BC.USD("aaa", "bbb"))), [])
        self.assertListEqual(Dolar_BC.USD.show_values((Dolar_BC.USD("31/01/2023", "31/04/2022"))), [])

    def test_USD2BRL(self):
        self.assertDictEqual(Dolar_BC.USD.USD2BRL((Dolar_BC.USD("31/01/2023", "01/02/2023")), 0.00),{"Value of conversion (buy)": 0.00,
                                                                                                     "Value of conversion (sell)": 0.00})
        self.assertRaises("TypeError: can't multiply sequence by non-int of type 'float'", Dolar_BC.USD.USD2BRL((Dolar_BC.USD("31/01/2023", "01/02/2023")), "ssss"))
        self.assertDictEqual(Dolar_BC.USD.USD2BRL((Dolar_BC.USD("31/01/2023", "01/02/2023")), -100000.0),
                                                                                            {"Value of conversion (buy)": -19612842489261968737129072116422.0,
                                                                                                    "Value of conversion (sell)": -196.12842489261968737129072116422}, "ok")
        self.assertDictEqual(Dolar_BC.USD.USD2BRL((Dolar_BC.USD("31/01/2023", "01/02/2023")), 2000000.0),{"Value of conversion (buy)": 10197400.0,
                                                                                                    "Value of conversion (sell)": 10198600.0})
    def test_BRL2USD(self):
        self.assertDictEqual(Dolar_BC.USD.USD2BRL((Dolar_BC.USD("31/01/2023", "01/02/2023")), 0.00),{"Value of conversion (buy)": 0.00,
                                                                                                     "Value of conversion (sell)": 0.00})
        self.assertRaises("TypeError: can't multiply sequence by non-int of type 'float'", Dolar_BC.USD.USD2BRL((Dolar_BC.USD("31/01/2023", "01/02/2023")), "ssss"))
        self.assertDictEqual(Dolar_BC.USD.USD2BRL((Dolar_BC.USD("31/01/2023", "01/02/2023")), -2000000.0),{"Value of conversion (buy)": -10143000.0,
                                                                                                    "Value of conversion (sell)": -10144200})
        self.assertDictEqual(Dolar_BC.USD.USD2BRL((Dolar_BC.USD("31/01/2023", "01/02/2023")), 1000000.0),{"Value of conversion (buy)": 5071500.0,
                                                                                                    "Value of conversion (sell)": 5072100.0})
if __name__ == '__main__':
    unittest.main()
