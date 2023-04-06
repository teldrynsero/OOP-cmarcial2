from __future__ import annotations

"""Cup class
"""

from mutable import Solver
from typing import cast, Iterable

class Cup(Solver):
    """Cup class
    """
    def __init__(self, n: int, cups: list[str]) -> None:
        """Constructor

        Args:
            cups (str): cup color and diameter
        """
        self._n = n
        self._cups = cups

    def set_values(self, n: int, cups: list[str]) -> None:
        """Sets data to n

        Args:
            cups (str): cup color and diameter
        """
        self._n = n
        self._cups = cups

    @property
    def getN(self) -> int:
        """return n value

        Returns:
            str: n value
        """
        return self._n
    
    @property
    def getData(self) -> list[str]:
        """return cup data

        Returns:
            str: cup data
        """
        return self._cups

    @property
    def solve(self) -> str:
        """Returns the diameter of cup

        Returns:
            int: diameter
        """
        diameter = []
        color = []
        x = 0
        while self._n != 0:
            singleData = self._cups[x].split()
            digitData = singleData[0].isdigit()
            if digitData == True:
                trueDiameter = int(singleData[0])/2
                diameter.append(trueDiameter)
                color.append(singleData[1])
            else:
                diameter.append(int(singleData[1]))
                color.append(singleData[0])
            self._n -= 1
            x += 1

        #print(diameter)
        result = zip(diameter,color)
        tupledList = list(result)
        tupledList.sort()

        n = 1
        orderedColors = [x[n] for x in tupledList]
        #print(orderedColors)
        answer = '\n'.join(cast(Iterable[str], orderedColors))

        return answer
    
    @property
    def getSolve(self) -> str:
        """return solved data

        Returns:
            List: solved data
        """
        return self.solve
    
    def __str__(self) -> str:
        """Returns string rep of object

        Returns:
            str: string rep
        """
        return str(self.solve)
    
    def __repr__(self) -> str:
        """Return string rep of object

        Returns:
            str: string rep
        """
        return self.__str__()