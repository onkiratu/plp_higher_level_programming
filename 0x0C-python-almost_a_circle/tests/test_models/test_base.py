#!/usr/bin/python3
"""module defines tests for Base class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ This class tests the Base class"""

    def test_without_id(self):
        """Test id without passing any argument"""
        result = Base()
        self.assertEqual(result.id, 1)


    def test_with_id(self):
        """Test id while passing an argument"""
        result = Base(15)
        self.assertEqual(result.id, 15)
