from __future__ import annotations

__author__ = "Christina Marcial"

from cup import Cup
from typing import Any, List
import sys
from kattis import Kattis

class Solution(Kattis):
    """Solution concrete class
    """
    def __init__(self, input_source: Any = sys.stdin) -> None:
        """Constructor
        """
        super().__init__(input_source)
        self._cupNumber: int = 0
        self._data: List[str] = []
        self._answer: List[str] = []
        self.read_input()

    def read_input(self) -> None:
        """Reads the data from the given source
        """
        data = self._input_source.readlines()
        self._cupNumber = int(data[0])
        self._data = [str(data[i]) for i in range(1, len(data))]
        #print(self._cupNumber)
        res = []
        for sub in self._data:
            res.append(sub.replace("\n",""))
        self._data = res
        #print(self._data)

    def data(self) -> List[str]:
        """Returns data

        Returns:
            List[str]: data
        """
        return self._data
    
    @property
    def answer(self) -> str:
        """Returns the answer

        Returns:
            str: answer
        """
        return '\n'.join([str(t) for t in self._answer])
    
    def solve(self) -> None:
        """Solves the problem
        """
        self._answer = [str(Cup(self._cupNumber,self._data))]
        self._answer.append('')

    def print_answer(self) -> None:
        """Prints answer
        """
        sys.stdout.write(self.answer)

if __name__ == "__main__":
    solution = Solution()
    solution.solve()
    solution.print_answer()