# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import unittest

import intelmq.lib.test as test
from intelmq.bots.parsers.vxvault.parser import VXVaultParserBot

EXAMPLE_REPORT = {"feed.name": "VxVault",
                  "feed.url": "http://vxvault.siri-urz.net/URL_List.php",
                  "raw": "VlggVmF1bHQgbGFzdCAxMDAgTGlua3MKTW9uLCAxNyBBdWcgMjAx"
                         "NSAxNDozNjoxOSArMDAwMAoKaHR0cDovL2V4YW1wbGUuY29tL2Jh"
                         "ZC9wcm9ncmFtLmV4ZQ==",
                  "__type": "Report",
                  "time.observation": "2015-01-01T00:00:00+00:00",
                  }
EXAMPLE_EVENT = {"feed.name": "VxVault",
                 "feed.url": "http://vxvault.siri-urz.net/URL_List.php",
                 "source.url": "http://example.com/bad/program.exe",
                 "classification.type": "malware",
                 "__type": "Event",
                 "raw": "aHR0cDovL2V4YW1wbGUuY29tL2JhZC9wcm9ncmFtLmV4ZQ==",
                 "source.fqdn": "example.com",
                 "time.observation": "2015-01-01T00:00:00+00:00",
                 }


class TestVXVaultParserBot(test.BotTestCase, unittest.TestCase):
    """
    A TestCase for VXVaultParserBot.
    """

    @classmethod
    def set_bot(cls):
        cls.bot_reference = VXVaultParserBot
        cls.default_input_message = json.dumps(EXAMPLE_REPORT)

    def test_event(self):
        """ Test if correct Event has been produced. """
        self.run_bot()
        self.assertMessageEqual(0, EXAMPLE_EVENT)


if __name__ == '__main__':
    unittest.main()
