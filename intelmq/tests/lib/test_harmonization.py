# -*- coding: utf-8 -*-
"""
Testing harmonization classes
"""
from __future__ import unicode_literals

import unittest

import intelmq.lib.harmonization as harmonization


class TestHarmonization(unittest.TestCase):

    def test_boolean_valid_bool(self):
        """ Test Boolean.is_valid with bool values. """
        self.assertTrue(harmonization.Boolean.is_valid(True))
        self.assertTrue(harmonization.Boolean.is_valid(False))

    def test_boolean_valid_other(self):
        """ Test Boolean.is_valid with otehr invalid values. """
        self.assertFalse(harmonization.Boolean.is_valid(None))
        self.assertFalse(harmonization.Boolean.is_valid('True'))
        self.assertFalse(harmonization.Boolean.is_valid(0))
        self.assertFalse(harmonization.Boolean.is_valid(1))
        self.assertFalse(harmonization.Boolean.is_valid([]))

    def test_boolean_sanitize_bool(self):
        """ Test Boolean.sanitize with bool values. """
        self.assertTrue(harmonization.Boolean.is_valid(True, sanitize=True))
        self.assertTrue(harmonization.Boolean.is_valid(False, sanitize=True))

    def test_boolean_sanitize_valid(self):
        """ Test Boolean.sanitize with valid string and int values. """
        self.assertTrue(harmonization.Boolean.is_valid(0, sanitize=True))
        self.assertTrue(harmonization.Boolean.is_valid(1, sanitize=True))
        self.assertTrue(harmonization.Boolean.is_valid('true', sanitize=True))
        self.assertTrue(harmonization.Boolean.is_valid('false', sanitize=True))

    def test_boolean_sanitize_invalid(self):
        """ Test Boolean.sanitize with invalid values. """
        self.assertFalse(harmonization.Boolean.is_valid(None, sanitize=True))
        self.assertFalse(harmonization.Boolean.is_valid([], sanitize=True))
        self.assertFalse(harmonization.Boolean.is_valid('test', sanitize=True))

    def test_integer_valid_int(self):
        """ Test Integer.is_valid with integer values. """
        self.assertTrue(harmonization.Integer.is_valid(-4532))
        self.assertTrue(harmonization.Integer.is_valid(1337))

    def test_integer_valid_other(self):
        """ Test Integer.is_valid with invalid values. """
        self.assertFalse(harmonization.Integer.is_valid('1337'))
        self.assertFalse(harmonization.Integer.is_valid(True))

    def test_integer_sanitize_int(self):
        """ Test Integer.sanitize with integer values. """
        self.assertTrue(harmonization.Integer.is_valid(-4532, sanitize=True))
        self.assertTrue(harmonization.Integer.is_valid(1337, sanitize=True))

    def test_integer_sanitize_other(self):
        """ Test Integer.sanitize with integer values. """
        self.assertTrue(harmonization.Integer.is_valid(True, sanitize=True))
        self.assertTrue(harmonization.Integer.is_valid('1337', sanitize=True))
        self.assertTrue(harmonization.Integer.is_valid(b'1337', sanitize=True))
        self.assertTrue(harmonization.Integer.is_valid(' 1337', sanitize=True))

    def test_integer_sanitize_invalid(self):
        """ Test Integer.sanitize with invalid values. """
        self.assertFalse(harmonization.Integer.is_valid(None, sanitize=True))
        self.assertFalse(harmonization.Integer.is_valid('b13', sanitize=True))

    def test_float_valid_flaot(self):
        """ Test Float.is_valid with flaot and integer values. """
        self.assertTrue(harmonization.Float.is_valid(-4532))
        self.assertTrue(harmonization.Float.is_valid(1337))
        self.assertTrue(harmonization.Float.is_valid(1337.2354))
        self.assertTrue(harmonization.Float.is_valid(13.234e-4))

    def test_float_valid_other(self):
        """ Test Float.is_valid with invalid values. """
        self.assertFalse(harmonization.Float.is_valid('1337.234'))
        self.assertFalse(harmonization.Float.is_valid(True))

    def test_float_sanitize_number(self):
        """ Test Float.sanitize with integer and float values. """
        self.assertTrue(harmonization.Float.is_valid(-4532.234, sanitize=True))
        self.assertTrue(harmonization.Float.is_valid(13.234e-4, sanitize=True))

    def test_float_sanitize_other(self):
        """ Test Float.sanitize with integer values. """
        self.assertTrue(harmonization.Float.is_valid(True, sanitize=True))
        self.assertTrue(harmonization.Float.is_valid('+137.23', sanitize=True))
        self.assertTrue(harmonization.Float.is_valid(b'17.234', sanitize=True))
        self.assertTrue(harmonization.Float.is_valid(' 1337.2', sanitize=True))
        self.assertTrue(harmonization.Float.is_valid('3.31e+3', sanitize=True))
        self.assertTrue(harmonization.Float.is_valid('-31.e-2', sanitize=True))

    def test_float_sanitize_invalid(self):
        """ Test Float.sanitize with invalid values. """
        self.assertFalse(harmonization.Float.is_valid(None, sanitize=True))
        self.assertFalse(harmonization.Float.is_valid('b13.23', sanitize=True))

    def test_ipaddress_valid(self):
        """ Test IPAddress.is_valid with valid arguments. """
        self.assertTrue(harmonization.IPAddress.is_valid('192.0.2.1'))
        self.assertTrue(harmonization.IPAddress.is_valid('::1'))
        self.assertTrue(harmonization.IPAddress.is_valid('2001:500:88:200::8'))

    def test_ipaddress_valid_invalid(self):
        """ Test IPAddress.is_valid with invalid arguments. """
        self.assertFalse(harmonization.IPAddress.is_valid('192.0.2.1/24'))
        self.assertFalse(harmonization.IPAddress.is_valid('2001:DB8::/32'))
        self.assertFalse(harmonization.IPAddress.is_valid('localhost'))

    def test_ipaddress_sanitize(self):
        """ Test IPAddress.is_valid and sanitize with valid arguments. """
        self.assertTrue(harmonization.IPAddress.is_valid(' 192.0.2.1\r\n',
                                                         sanitize=True))
        self.assertTrue(harmonization.IPAddress.is_valid(b'2001:DB8::1',
                                                         sanitize=True))

    def test_ipaddress_sanitize_invalid(self):
        """ Test IPAddress.is_valid ans sanitize with invalid arguments. """
        self.assertFalse(harmonization.IPAddress.is_valid(' 192.0.2.0/24\r\n',
                                                          sanitize=True))
        self.assertFalse(harmonization.IPAddress.is_valid(b'2001:DB8::1/32',
                                                          sanitize=True))

    def test_ipnetwork_valid(self):
        """ Test IPNetwork.is_valid with valid arguments. """
        self.assertTrue(harmonization.IPNetwork.is_valid('192.0.2.1'))
        self.assertTrue(harmonization.IPNetwork.is_valid('::1'))
        self.assertTrue(harmonization.IPNetwork.is_valid('192.0.2.0/24'))
        self.assertTrue(harmonization.IPNetwork.is_valid('2001:DB8::/32'))
        self.assertTrue(harmonization.IPNetwork.is_valid('2001:500:88:200::8'))

    def test_ipnetwork_valid_invalid(self):
        """ Test IPNetwork.is_valid with invalid arguments. """
        self.assertFalse(harmonization.IPNetwork.is_valid('localhost'))
        self.assertFalse(harmonization.IPNetwork.is_valid('192.0.2.1/37'))
        self.assertFalse(harmonization.IPNetwork.is_valid('192.0.2.1/0'))
        self.assertFalse(harmonization.IPNetwork.is_valid('2001:DB8::/130'))

    def test_ipnetwork_sanitize(self):
        """ Test IPNetwork.is_valid and sanitize with valid arguments. """
        self.assertTrue(harmonization.IPNetwork.is_valid(' 192.0.2.0/24\r\n',
                                                         sanitize=True))
        self.assertTrue(harmonization.IPNetwork.is_valid(b'2001:DB8::/32',
                                                         sanitize=True))

    def test_ipnetwork_sanitize_invalid(self):
        """ Test IPNetwork.is_valid and sanitize with invalid arguments. """
        self.assertFalse(harmonization.IPNetwork.is_valid(' 192.0.2.0/-4\r\n',
                                                          sanitize=True))
        self.assertFalse(harmonization.IPNetwork.is_valid(b'2001:DB8Z::1/7',
                                                          sanitize=True))

    def test_datetime_from_timestamp(self):
        """ Test DateTime.from_timestamp method. """
        self.assertEqual('2015-08-31T08:16:10+00:00',
                         harmonization.DateTime.from_timestamp(1441008970))
        self.assertEqual('2015-08-31T07:16:10-01:00',
                         harmonization.DateTime.from_timestamp(1441008970,
                                                               'Etc/GMT+1'))
        self.assertEqual('2015-08-31T04:16:10-04:00',
                         harmonization.DateTime.from_timestamp(1441008970,
                                                               'America/'
                                                               'Guyana'))

    def test_datetime_from_timestamp_invalid(self):
        """ Test DateTime.from_timestamp method with invalid inputs. """
        with self.assertRaises(TypeError):
            harmonization.DateTime.from_timestamp('1441008970')

if __name__ == "__main__":
    unittest.main()
