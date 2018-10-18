import unittest
from unittest.mock import patch

import requests

from models import XRate, init_db
import main


def get_privat_response():
    return [{"ccy": "USD", "base_ccy": "UAH", "sale": "30.0"}]


def get_privat_error_response():
    return [{"ccy": "USD", "base": "UAH", "sale": "30.0"}]


class Test(unittest.TestCase):

    def setUp(self):
        print("in setUp")
        init_db()

    def _test_privat_timeout(self):
        # self.assertRaises(requests.exceptions.ReadTimeout, main.update_from_privat_api)
        main.update_from_privat_api()

        for from_currency, to_currency in (("USD", "UAH"), ("RUR", "UAH"), ("EUR", "UAH")):
            rate = XRate.get_or_none(from_currency=from_currency,
                                     to_currency=to_currency)

            self.assertIsNotNone(rate)
            self.assertNotEqual(rate.rate, 1.0)

    @patch("main.get_rates_from_privat", new=get_privat_response)
    def test_privat_mock(self, ):
        main.update_from_privat_api()

        rate = XRate.get_or_none(from_currency="USD", to_currency="UAH")

        self.assertIsNotNone(rate)
        self.assertEqual(rate.rate, 30)

        rates_count = XRate.select().count()
        self.assertEqual(rates_count, 1)

    @patch("main.get_rates_from_privat", new=get_privat_error_response)
    def test_privat_mock_error(self):

        self.assertRaises(main.ResponseException, main.update_from_privat_api)

    @patch("main.PrivatApi")
    def test_privat_class_mock(self, PrivatMock):
        PrivatMock().get_rates.return_value = get_privat_response()

        main.update_from_privat_api()

        rate = XRate.get_or_none(from_currency="USD", to_currency="UAH")

        self.assertIsNotNone(rate)
        self.assertEqual(rate.rate, 30)
        self.assertTrue(PrivatMock.called)


if __name__ == '__main__':
    unittest.main()
