from __future__ import annotations

import unittest
import sys
from main import Solution
from unittest.mock import patch
from io import StringIO
from hypothesis import given
from hypothesis.strategies import text

class TestMain(unittest.TestCase):
	"""Unittests for Solution class

	"""
	def setUp(self) -> None:
		"""Set up

		"""
		data = "8 4\n1073741824 1073741820\n6 20\n99999 1\n0 0"
		with patch('sys.stdin', StringIO(data)):
			self.sol = Solution(sys.stdin)

	@given(text())
	def test_getData(self,s):
		"""tests getData method 

		"""
		self.assertEqual(self.sol.getData(),['8 4\n', '1073741824 1073741820\n', '6 20\n', '99999 1\n', '0 0'])

	@given(text())
	def test_getAnswer(self,s):
		"""tests getAnswer method 
		
		"""
		self.assertEqual(self.sol.getAnswer(),['2 0 / 4', '1 4 / 1073741820', '0 6 / 20', '99999 0 / 1', '', ''])

	@patch('sys.stdout', new_callable=StringIO)
	def test_solve(self, mock_stdout: StringIO) -> None:
		"""Tests solve method

		"""
		expected =  "2 0 / 4\n1 4 / 1073741820\n0 6 / 20\n99999 0 / 1\n\n"
		self.sol.solve()
		self.assertEqual(mock_stdout.getvalue(), expected)

if __name__ == '__main__':
	unittest.main(verbosity=2)