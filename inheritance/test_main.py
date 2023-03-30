from __future__ import annotations

import unittest
import sys
from main import Solver
from data import Data
from unittest.mock import patch
from io import StringIO
from hypothesis import given, strategies as st
from hypothesis.strategies import lists
from dataclasses import dataclass

class TestMain(unittest.TestCase):
	"""Unittests for Solver class

	"""
	def setUp(self) -> None:
		"""Set up

		"""
		self.data = "10 1 2 3 4 5 7 6 8 9 10\n2 300 301\n6 5 500 50 555 5555 5050"
		with patch('sys.stdin', StringIO(self.data)):
			self.sol = Solver(sys.stdin)

	def test_getData(self) -> None:
		"""tests getData method 

		"""
		self.assertEqual(self.sol.getData(),['10 1 2 3 4 5 7 6 8 9 10', '2 300 301', '6 5 500 50 555 5555 5050'])

	def test_solve(self) -> None:
		"""Tests solve method + getAnswer
		"""
		self.assertEqual(self.sol.solve(), ['Case 1: 1 10 9', 'Case 2: 300 301 1', 'Case 3: 5 5555 5550'])
		self.assertEqual(self.sol.getAnswer(), ['Case 1: 1 10 9', 'Case 2: 300 301 1', 'Case 3: 5 5555 5550'])
		
	def test_solve1(self) -> None:
		"""Tests solve method  + getAnswer 2nd data
		"""
		self.sol.data = ['1 10000', '3 600 690 691']
		self.assertEqual(self.sol.solve(), ['Case 1: 10000 10000 0', 'Case 2: 600 691 91'])
		self.assertEqual(self.sol.getAnswer(), ['Case 1: 10000 10000 0', 'Case 2: 600 691 91'])

	@patch('sys.stdout', new_callable=StringIO)
	def test_printAnswer(self, mock_stdout: StringIO) -> None:
		"""Tests printAnswer method
		"""
		self.sol.solve()
		self.sol.printAnswer()
		expected = 'Case 1: 1 10 9\nCase 2: 300 301 1\nCase 3: 5 5555 5550\n'
		self.assertEqual(mock_stdout.getvalue(), expected)

	@patch('sys.stdout', new_callable=StringIO)
	def test_printAnswer1(self, mock_stdout: StringIO) -> None:
		"""Tests printAnswer method 2nd data
		"""
		self.sol.data = ['1 10000', '3 600 690 691']
		self.sol.solve()
		self.sol.printAnswer()
		expected = 'Case 1: 10000 10000 0\nCase 2: 600 691 91\n'
		self.assertEqual(mock_stdout.getvalue(), expected)

	@given(st.text())
	def test_dataIsString(self,s):
		"""test getData returns correct type

		Args:
			s (string): user input data
		"""
		self.sol.data = s
		self.assertEqual(self.sol.getData(),s)

if __name__ == '__main__':
	unittest.main(verbosity=2)