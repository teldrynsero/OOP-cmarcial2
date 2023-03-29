from __future__ import annotations
__author__ = "Christina Marcial"

"""
Kattis Problem - Statistics
https://open.kattis.com/problems/statistics
"""
import sys
from data import Data
from typing import Any, List

class Solver(Data): #solve data
    def __init__(self, source:Any):
        """Using inputted data, solve for answers

        Args:
            source (Any): user input
        """
        Data.__init__(self, source)

    def solve(self) -> List[str]:
        """Solves the kattis problem
        """
        for n, data in enumerate(self.data): #for every set of numbers in the list...

            data = self.data[n]
            splitValues = data.split()
            dataInts = [int(i) for i in splitValues] #convert into ints
            dataInts.pop(0)

            answerForSet = "Case " + str(n+1) + ": " + str(min(dataInts)) + " " + str(max(dataInts)) + " " + str(max(dataInts) - min(dataInts))
            self.answer.append(answerForSet)

        return self.answer
        
    def getSolve(self) -> List[str]:
        """Returns answers

        Returns:
            List[str]: answers
        """
        return self.solve()
        
if __name__ == "__main__":
        solution = Solver(sys.stdin) #get input
        solution.solve() #solve
        solution.printAnswer() #print answer