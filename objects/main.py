__author__ = "Christina Marcial"

"""
Kattis Problem - Convex Polygon Area
https://open.kattis.com/problems/convexpolygonarea
"""
import sys
from polygon import Polygon
from typing import Any, List

class Solution(object):
    def __init__(self, source:Any):
        """
        Represents a solution to the problem
        """
        self._n: int = 0 # number of polygons
        self._data: List[str] = [] # data
        self._answer: List[str] = [] # list of area answers
        self.readData(source)
        self.findAnswer()

    def readData(self, source: Any) -> None:
        """
        Reads data
        return: none
        """

        data = sys.stdin.readlines()
        self._n = int(data[0])
        self._data = [str(data[i]) for i in range(1, len(data))]

        self.findAnswer()

    def findAnswer(self) -> None:
        """
        Calculates the area of the polygon
        :return: the area
        """
        res = [] #sets of polygon data
        for sub in self._data:
               res.append(sub.replace("\n", "")) #get rid of \n so only numbers remain

        #print("self._n: ")
        #print(self._n)
        #print("res: ")
        #print(res)

        self._answer = [str(Polygon(res)) for res in self._data]
        self._answer.append('')
        #print("self._answer: ")
        #print(self._answer)

    def getAnswer(self) -> List[str]:
        return self._answer

    def getN(self) -> int:
        """
        Returns the number of polygons
        :return: number of polygons
        """
        return self._n

    def getData(self) -> List[str]:
        """
        Returns the data
        :return: data
        """
        return self._data

    def solve(self) -> None:
        """
        Solves the problem
        :return: none
        """
        sys.stdout.write('\n'.join(self._answer))

if __name__ == "__main__":
        solution = Solution(sys.stdin)
        solution.solve()