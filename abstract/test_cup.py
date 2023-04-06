from __future__ import annotations

import unittest
from cup import Cup
from hypothesis import given, strategies as st

class TestCup(unittest.TestCase):
	"""
	Unit tests for Cup class
	"""
	def setUp(self) -> None:
		"""Set up
		
		"""
		self.data = Cup(2,['white 292','856 black'])

	def test_getName(self):
		"""Tests getData and getN method

		"""
		self.assertEqual(self.data.getData,['white 292','856 black'])
		self.assertEqual(self.data.getN,2)

	def test_solve(self):
		"""Tests solve method

		"""
		self.assertEqual(self.data.solve, 'white\nblack')

	def test_getSolve(self):
		"""Test getSolve methodpyt

		"""
		self.data.set_values(2,['white 292','856 black'])
		self.assertEqual(str(self.data), 'white\nblack')

	@given(s=st.integers())
	def test_hypo(self, s):
		"""Using hypothesis, assert cups number is 2
		"""
		s = 2
		self.assertEqual(self.data._n, s)	

if __name__ == '__main__':
	unittest.main(verbosity=2)