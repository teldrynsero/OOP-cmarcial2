__author__ = "Christina Marcial"

"""
Polygon Class
"""

class Polygon(object):
    def __init__(self, n: str) -> None:
        """
        Constructor
        """
        self.n = n

    def setN(self, n: str) -> None:
        """
        Set up n
        :param n: n
        """
        self.n = n

    @property
    def getN(self) -> str:
        """
        Returns n
        :return: n
        """
        return self.n

    def solve(self) -> str:
        """
        Solve polygon data for area
        :return: area
        """

        #print("ENTERED POLYGON.PY")

        #print("n: ")
        #print(self.n)

        data = self.n
        num = 0
        counter = 0
        area = 0.0

        x = [] #array of x coordinate values
        y = [] #array of y coordinate values
        
        newData = data.split() #convert string data into array

        dataInts = [int(i) for i in newData] #convert into ints

        for i in dataInts: #split data into x and y coordinates
            if (counter == 0):
                num = i #first value isn't part of the coordinates
            elif (counter % 2 == 0):
                y.append(i) #is a y coordinate
            else:
                x.append(i) #is a x coordinate
            counter = counter + 1

        #print("num: ")
        #print(num)
        #print("x coords:")
        #print(x)
        #print("y coords:")
        #print(y)

        #equation to solve for polygon area
        j = num - 1
        for i in range(0,num):
            area += (x[j] + x[i]) * (y[j] - y[i])
            j = i

        #return area
        return f'{float(abs(area / 2.0)):g}' #:g gets rid of leading 0s

    def getSolve(self) -> str:
        """
        :return: solve
        """
        return self.solve()

    def __str__(self) -> str:
        """
        :return: getSolve
        """
        return f'{self.getSolve()}'

    def _repr_(self) -> str:
        return self.__str__()