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
		self._answer: int = 0 # answer?
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
		"""_summary_

		Returns:
			_type_: _description_
		"""

		self._answer = str(Morse(self._word))

	def get_answer(self) -> int:
		"""_summary_

		Returns:
			int: _description_
		"""
		return self._answer

	def get_word(self) -> str:
		"""get given word

		Returns:
			str: word
		"""
		return self._word

	def solve(self) -> None:
		"""_summary_

		Args:
			source (Any): _description_
		"""
		#self.read_word(source)
		#print(self.find_answer())
		#sys.stdout.write('1')
		#sys.stdout.write("\n")
		#sys.stdout.write("self._answer: ")
		sys.stdout.write(self._answer + "\n")
		#sys.stdout.write('\n'.join(self._answer))
		#sys.stdout.write("\n")
		#print(self._answer)
		#print("\n")

if __name__ == "__main__":
        solution = Solution(sys.stdin)
        solution.solve()