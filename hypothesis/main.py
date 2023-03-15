from __future__ import annotations

__author__ = "Christina Marcial"

"""
Kattis Problem - Title Cost
https://open.kattis.com/problems/titlecost
"""

import sys
from title import Title
from typing import Any

class Solution(object):
	def __init__(self, source:Any):
		"""
		solution to problem
		"""
		self._name: str = '' # given input string
		self._answer: str = '' # answer
		self.read_name(source)
		self.find_answer()
		
	def read_name(self, source: Any) -> None:
		"""reads given word

		Args:
			source (Any): user input
		"""
		data = source.read()
		#print("data: ")
		#print(data)
		self._name = str(data)

		self.find_answer()

	def find_answer(self) -> None:
		"""finds answer by calling function

		Returns:
			None
		"""

		self._answer = str(Title(self._name))

	def get_answer(self) -> str:
		"""Returns answer

		Returns:
			str: answer
		"""
		return self._answer

	def get_name(self) -> str:
		"""Get given string

		Returns:
			str: name
		"""
		return self._name

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