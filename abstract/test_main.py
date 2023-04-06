from __future__ import annotations

import unittest
import sys
from main import Solution
from unittest.mock import patch
from io import StringIO
from hypothesis import given, strategies as st

class TestMain(unittest.TestCase):
	"""Unittests for Main class

	"""
	def setUp(self) -> None:
		"""Set up

		"""
		self.data = "5\n50 green\n1 pink\ngreen 511\npink 20\nwhite 100"
		with patch('sys.stdin', StringIO(self.data)):
			self.sol = Solution(sys.stdin)

	def test_data(self) -> None:
		"""tests data method 

		"""
		self.assertEqual(self.sol.data(),['50 green', '1 pink', 'green 511', 'pink 20', 'white 100'])

	@patch('sys.stdout', new_callable=StringIO)
	def test_print_answer(self, mock_stdout: StringIO) -> None:
		"""Tests print_answer and answer method
		"""
		self.sol.solve()
		self.sol.print_answer()
		expected = 'pink\npink\ngreen\nwhite\ngreen\n'
		self.assertEqual(mock_stdout.getvalue(), expected)
		self.assertEqual(self.sol.answer, expected)

	@given(s=st.integers())
	def test_hypo(self, s):
		"""Using hypothesis, assert cupnumber is int 5
		"""
		s = 5
		self.assertEqual(self.sol._cupNumber, s)	

if __name__ == '__main__':
	unittest.main(verbosity=2)