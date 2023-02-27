import unittest
from morse import Morse

class TestMorse(unittest.TestCase):
	"""
	Unit tests for Odd class
	"""
	def setUp(self) -> None:
		"""Set up
		
		"""
		self.morse = Morse('mom')

	def test_setWord(self) -> None:
		"""Tests set_word method
		
		"""
		self.morse.set_word('mom')
		self.assertEqual(self.morse.get_word(), 'mom')

	def test_getWord(self) -> None:
		"""Tests get_word method
		"""
		self.assertEqual(self.morse.get_word(), 'mom')

	def test_solve(self) -> None:
		"""Tests solve method
		"""
		self.assertEqual(self.morse.solve(), 1)

	def test_solve1(self) -> None:
		"""Tests solve method 2nd data
		"""
		self.morse.set_word('###')
		self.assertEqual(self.morse.solve(), 0)

	def test_solve2(self) -> None:
		"""Tests solve method 3rd data
		"""
		self.morse.set_word('Obi-Wan Kenobi')
		self.assertEqual(self.morse.solve(), 0)

	def test_getSolve(self) -> None:
		"""Tests get_solve method
		"""
		self.assertEqual(str(self.morse), '1')

	def test_getSolve1(self) -> None:
		"""Tests get_solve method 2nd data
		"""
		self.morse.set_word('###')
		self.assertEqual(str(self.morse), '0')

	def test_getSolve2(self) -> None:
		"""Tests get_solve method 3rd data
		"""
		self.morse.set_word('Obi-Wan Kenobi')
		self.assertEqual(str(self.morse), '0')

if __name__ == '__main__':
	unittest.main(verbosity=2)