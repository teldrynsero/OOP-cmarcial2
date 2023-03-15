from __future__ import annotations

__author__ = "Christina Marcial"

from typing import overload

class Title(object):
	"""Class for finding title cap answer
	"""
	def __init__(self, name: str) -> None:
		"""

		Args:
			word (str): given word
		"""
		self.name = name
		
	def set_name(self, name: str) -> None:
		"""Set name

		Args:
			name (str): movie name and cap
		"""
		self.name = name

	def get_name(self) -> str:
		"""Get name

		Returns:
			str: name
		"""
		return self.name
	
	def solve(self) -> float:
		"""Returns the cost to transmit the title

		Returns:
			float: cost
		"""
		#print("self.name: ")
		#print(self.name)
		name = self.name
		separatedList = name.split()
		#print("separatedList: ")
		#print(separatedList)

		nameLength = len(separatedList[0])
		#print("nameLength: ")
		#print(nameLength)

		cost = ""

		capCost = separatedList[1]

		if float(nameLength) > float(capCost):
			cost = capCost
		else:
			cost = str(nameLength)

		return float(cost)

	def get_solve(self) -> float:
		"""Get solution

		Returns:
			float: solution
		"""
		return self.solve()
	
	def __str__(self) -> str:
		"""String rep of answer

		Returns:
			str: solution as string
		"""
		return f'{self.get_solve()}'

	def _repr_(self) -> str:
		"""Return string rep

		Returns:
			str: string rep
		"""
		return self.__str__()