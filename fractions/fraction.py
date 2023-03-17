from __future__ import annotations
__author__ = "Christina Marcial"

"""
Fraction Class
"""

class Fraction(object):
    def __init__(self, n: str) -> None:
        """Constructor

        """
        self.n = n #fraction

    def setN(self, n: str) -> None:
        """Set up n

        Args:
            n (str): fraction to solve
        """
        self.n = n

    def getN(self) -> str:
        """Returns n

        Returns:
            str: fraction to solve
        """
        return self.n

    def solve(self) -> str:
        """Converts fraction into mixed

        Returns:
            str: converted fraction
        """

        splitValues = self.n.split()
        #print(splitValues)
        if splitValues == ['0','0']:
            return ""
        else:
            intValues = [eval(i) for i in splitValues] #turn list of strings into list of ints
            #print("List: ", intValues)

            #intValues[0] = num
            #intValues[1] = dem

            a = intValues[0] // intValues[1]
            b = intValues[0] % intValues[1]

            answer = str(a) + " " + str(b) + " / " + str(intValues[1])

            #print("answer: ")
            #print(answer)

            return answer

    def getSolve(self) -> str:
        """Returns solve

        Returns:
            str: converted fraction
        """
        return self.solve()

    def __str__(self) -> str:
        """String rep of object

        Returns:
            str: String rep of object
        """
        return f'{self.getSolve()}'

    def _repr_(self) -> str:
        """Returns string rep of object

        Returns:
            str: String rep of object
        """
        return self.__str__()