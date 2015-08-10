import os
import sys
import unittest2

sys.path.insert(0, os.path.abspath(".."))

import your_app.code

class TestCode(unittest2.TestCase):

	def test_squares_positive_numbers_correctly(self):

		self.assertEqual(your_app.code.square(2), 4)

	def test_squares_negative_numbers_correctly(self):

		self.assertEqual(your_app.code.square(-3), 9)