import unittest
from title import Title

class TestTitle(unittest.TestCase):
	"""
	Unit tests for Title class
	"""
	def setUp(self) -> None:
		"""Set up
		
		"""
		self.title = Title('ChickenRun 100.42069')

	def test_setName(self) -> None:
		"""Tests set_name method
		
		"""
		self.title.set_name('ChickenRun 100.42069')
		self.assertEqual(self.title.get_name(), 'ChickenRun 100.42069')

	def test_getName(self) -> None:
		"""Tests get_name method
		"""
		self.assertEqual(self.title.get_name(), 'ChickenRun 100.42069')

	def test_solve(self) -> None:
		"""Tests solve method
		"""
		self.assertEqual(self.title.solve(), 10.0)

	def test_solve1(self) -> None:
		"""Tests solve method 2nd data
		"""
		self.title.set_name('LordOfTheRings 2.1932194')
		self.assertEqual(self.title.solve(), 2.1932194)

	def test_solve2(self) -> None:
		"""Tests solve method 3rd data
		"""
		self.title.set_name('SpiritedAway 7.9939')
		self.assertEqual(self.title.solve(), 7.9939)

	def test_getSolve(self) -> None:
		"""Tests get_solve method
		"""
		self.assertEqual(str(self.title), '10.0')

	def test_getSolve1(self) -> None:
		"""Tests get_solve method 2nd data
		"""
		self.title.set_name('LordOfTheRings 2.1932194')
		self.assertEqual(str(self.title), '2.1932194')

	def test_getSolve2(self) -> None:
		"""Tests get_solve method 3rd data
		"""
		self.title.set_name('SpiritedAway 7.9939')
		self.assertEqual(str(self.title), '7.9939')

if __name__ == '__main__':
	unittest.main(verbosity=2)