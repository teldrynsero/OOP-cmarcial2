__author__ = "Christina Marcial"

"""
Kattis Problem - Morse Code Palindromes
https://open.kattis.com/problems/morsecodepalindromes
"""

import sys
from morse import Morse
from typing import Any, List

class Solution(object):
	def __init__(self, source:Any):
		"""
		solution to problem
		"""
		self._word: str = '' # the given input string
		self._answer: str = '' # answer?
		self.read_word(source)
		self.find_answer()

	def read_word(self, source: Any) -> None:
		"""reads given word

		Args:
			source (Any): user input
		"""

		data = source.read()
		#print("data: ")
		#print(data)
		self._word = str(data)
		self.find_answer()

	def find_answer(self) -> None:
		"""finds answer by calling function

		Returns:
			None
		"""

		self._answer = str(Morse(self._word))

	def get_answer(self) -> str:
		"""Returns answer

		Returns:
			str: answer
		"""
		return self._answer

	def get_word(self) -> str:
		"""Get given word

		Returns:
			str: word
		"""
		return self._word

	def solve(self) -> None:
		"""Print Answer

		Returns:
			None
		"""
		#sys.stdout.write("self._answer: ")
		sys.stdout.write(self._answer + "\n")


if __name__ == "__main__":
        solution = Solution(sys.stdin)
        solution.solve()