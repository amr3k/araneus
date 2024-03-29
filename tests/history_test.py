# -*- coding: utf-8; -*-
# LICENSE: see Araneus/LICENSE
import unittest
from Araneus.history import *


class TestHistory(unittest.TestCase):
    def test_create(self):
        self.assertTrue(History().create())

    def test_clear(self):
        self.assertTrue(History().clear())

    def test_append(self):
        self.assertTrue(History().add('amr'))

    def test_get(self):
        self.assertIsInstance(History().get(), list)

    def test_sanitise(self):
        self.assertTrue(History().sanitise())


if __name__ == '__main__':
    unittest.main()
