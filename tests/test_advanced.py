# -*- coding: utf-8 -*-

from .context import core

import unittest
import pandas as pd


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_import_data(self):
        self.assertIsInstance(core.import_data("data/Input.txt"), pd.DataFrame)

    def test_process_data(self):
        d = {'CLIENT TYPE': ['CL', 'CL'], 'CLIENT NUMBER': ['1234', '1234'], 'ACCOUNT NUMBER': [
            '0002', '0002'], 'SUBACCOUNT NUMBER': ['0001', '0001'], 'EXCHANGE CODE': ['SGX', 'SGX'], 'PRODUCT GROUP CODE': ['', ''],
            'SYMBOL': ['FUNK', 'FUNK'], 'EXPIRATION DATE': ['20100910', '20100910'], 'QUANTITY LONG': ['3', '0'], 'QUANTITY SHORT': ['0', '4']}
        df = pd.DataFrame(data=d)
        df = core.process_data(df)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df.index), 1)
        self.assertEqual(len(df.index), 1)
        self.assertEqual(df.iloc[0]['Total_Transaction_Amount'], -1)
        


if __name__ == '__main__':
    unittest.main()
