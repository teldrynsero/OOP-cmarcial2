import unittest
from fraction import Fraction
from hypothesis import given
from hypothesis.strategies import text

class TestFraction(unittest.TestCase):
	"""
	Unit tests for Fraction class
	"""
	def setUp(self) -> None:
		"""Set up
		
		"""
		self.fraction = Fraction('8 4')

	@given(text())
	def test_setname(self, s):
		"""Tests setN method
		
		"""
		self.fraction.setN('8 4')
		self.assertEqual(self.fraction.getN(), '8 4')

	@given(text())
	def test_getName(self, s):
		"""Tests getN method

		"""
		self.assertEqual(self.fraction.getN(),'8 4')

	@given(text())
	def test_solve(self, s):
		"""Tests solve method

		"""
		self.assertEqual(self.fraction.solve(), '2 0 / 4')

	@given(text())
	def test_getSolve(self, s):
		"""Test getSolve method

		"""
		self.fraction.setN('8 4')
		self.assertEqual(str(self.fraction), '2 0 / 4')

if __name__ == '__main__':
	unittest.main(verbosity=2)