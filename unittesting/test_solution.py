import unittest
import sys
from main import Solution
from unittest.mock import patch
from io import StringIO

class TestSolution(unittest.TestCase):
	"""
	Unit tests for Solution class
	"""
	def setUp(self) -> None:
		"""Set up

		"""
		data = 'mom'
		with patch('sys.stdin', StringIO(data)):
			self.sol = Solution(sys.stdin)

	def test_getWord(self) -> None:
		"""Tests get_word method

		"""
		self.assertEqual(self.sol.get_word(), 'mom')

	@patch('sys.stdout', new_callable=StringIO)
	def test_solve(self, mock_stdout: StringIO) -> None:
		"""Tests solve method

		"""
		self.sol.solve()
		expected = '1\n'
		self.assertEqual(mock_stdout.getvalue(), expected)

	@patch('sys.stdout', new_callable=StringIO)
	def test_solve1(self, mock_stdout: StringIO) -> None:
		"""Tests solve method 2nd data

		"""
		data = '###'
		with patch('sys.stdin', StringIO(data)):
			sol = Solution(sys.stdin)
			sol.solve()
			expected = '0\n'
			self.assertEqual(mock_stdout.getvalue(), expected)

	@patch('sys.stdout', new_callable=StringIO)
	def test_solve2(self, mock_stdout: StringIO) -> None:
		"""Tests solve method 3rd data

		"""
		data = 'Obi-Wan Kenobi'
		with patch('sys.stdin', StringIO(data)):
			sol = Solution(sys.stdin)
			sol.solve()
			expected = '0\n'
			self.assertEqual(mock_stdout.getvalue(), expected)

if __name__ == '__main__':
	unittest.main(verbosity=2)