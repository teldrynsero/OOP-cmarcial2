from __future__ import annotations

import unittest
import sys
from main import Solution
from unittest.mock import patch
from io import StringIO
from dataclasses import dataclass
from hypothesis import given, strategies as st

@dataclass
class GeneratedData:
	solve_value: st.SearchStrategy[str]
	
generated_data = GeneratedData(solve_value=st.characters())

class TestMain(unittest.TestCase):
	"""
	Unit tests for Main class
	"""
	def setUp(self) -> None:
		"""Set up

		"""
		data = 'StarWars 50.9'
		with patch('sys.stdin', StringIO(data)):
			self.sol = Solution(sys.stdin)

	def test_getName(self) -> None:
		"""Tests get_name method

		"""
		self.assertEqual(self.sol.get_name(), 'StarWars 50.9')

	def test_getAnswer(self) -> None:
		"""Tests get_answer method
		"""
		self.assertEqual(self.sol.get_answer(), '8.0')

	@patch('sys.stdout', new_callable=StringIO)
	def test_solve(self, mock_stdout: StringIO) -> None:
		"""Tests solve method

		"""
		self.sol.solve()
		expected = '8.0\n'
		self.assertEqual(mock_stdout.getvalue(), expected)

	@patch('sys.stdout', new_callable=StringIO)
	def test_solve1(self, mock_stdout: StringIO) -> None:
		"""Tests solve method 2nd data

		"""
		data = 'TopGun 1.541'
		with patch('sys.stdin', StringIO(data)):
			sol = Solution(sys.stdin)
			sol.solve()
			expected = '1.541\n'
			self.assertEqual(mock_stdout.getvalue(), expected)

	@patch('sys.stdout', new_callable=StringIO)
	def test_solve2(self, mock_stdout: StringIO) -> None:
		"""Tests solve method 3rd data

		"""
		data = 'Dune 4.999'
		with patch('sys.stdin', StringIO(data)):
			sol = Solution(sys.stdin)
			sol.solve()
			expected = '4.0\n'
			self.assertEqual(mock_stdout.getvalue(), expected)

if __name__ == '__main__':
	unittest.main(verbosity=2)
