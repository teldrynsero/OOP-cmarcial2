from __future__ import annotations
__author__ = "Christina Marcial"

"""
Data Class
"""

import sys
from typing import Any, List

class Data(object): #read data
        def __init__(self, source:Any):
            """Represents the inputted data to the problem

            Args:
                source (Any): User or sample input
            """
            self.data: List[str] = [] #data is list of strings
            self.answer: List[str] = [] #list of answers
            self.readData(source) #get inputted data

        def readData(self, source: Any) -> None:
            """Gets inputted data and removes unneeded characters

            Args:
                source (Any): User or sample input
            """
            data = sys.stdin.readlines()
            self.data = [str(data[i]) for i in range(0, len(data))]
            res = []
            for sub in self.data:
                  res.append(sub.replace("\n","")) #remove \n from data
            self.data = res #data got

        def getData(self) -> List[str]:
            """Get list of data

            Returns:
                List[str]: List of strings of data
            """
            return self.data

        def getAnswer(self) -> List[str]:
            """Returns answer
            Returns:
                List[str]: list of answers
            """
            return self.answer

        def printAnswer(self) -> None:
            """Prints answers
            """
            sys.stdout.write('\n'.join(self.answer))
            sys.stdout.write('\n')
