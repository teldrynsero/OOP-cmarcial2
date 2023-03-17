from __future__ import annotations
__author__ = "Christina Marcial"

"""
Kattis Problem - Mixed Fractions
https://open.kattis.com/problems/mixedfractions
"""
import sys
from fraction import Fraction
from typing import Any, List

class Solution(object):
    def __init__(self, source:Any):
        """Represents a solution to the problem

        """
        self._data: List[str] = [] # inputted fractions
        self._answer: List[str] = [] # list of reduced answers
        self.readData(source)
        self.findAnswer()

    def readData(self, source: Any) -> None:
        """Reads given data

        Args:
            source (Any): user input
        """
        data = sys.stdin.readlines()
        #self._n = int(data[0])
        self._data = [str(data[i]) for i in range(0, len(data))]

        self.findAnswer()

    def findAnswer(self) -> None:
        """Finds answer by calling function
        """
        res = [] #list of fractions
        for sub in self._data:
               res.append(sub.replace("\n", "")) #get rid of \n so only numbers remain

        self._answer = [str(Fraction(res)) for res in self._data]
        self._answer.append('')

    def getAnswer(self) -> List[str]:
        """Returns answer

        Returns:
            List[str]: list of answers
        """
        return self._answer

    def getData(self) -> List[str]:
        """Get given fractions

        Returns:
            List[str]: list of fractions
        """
        return self._data

    def solve(self) -> None:
        """Prints answers
        """
        sys.stdout.write('\n'.join(self._answer))

if __name__ == "__main__":
        solution = Solution(sys.stdin)
        solution.solve()