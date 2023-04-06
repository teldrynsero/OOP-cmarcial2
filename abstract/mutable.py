from __future__ import annotations

from abc import abstractmethod
import _collections_abc

class Solver(_collections_abc.MutableSequence):
    """Used to solve Kattis problem data
    """
    def __init__(self, n=None, data=None):
        """Data

        Args:
            n: number of data inputs
            data: data
        """
        self.n = n
        self.data = data

    @abstractmethod
    def set_values(self,n,data):
        """sets the data values

        Args:
            n: number of data inputs
            data: data
        """
        ...
    
    @property
    @abstractmethod
    def getN(self) -> any:
        """Returns n value

        Returns:
            any: n
        """
        ...

    @property
    @abstractmethod
    def getData(self) -> any:
        """Returns data

        Returns:
            any: data
        """
        ...

    @property
    @abstractmethod
    def solve(self) -> any:
        """Solves the problem

        Returns:
            any: answer
        """
        ...
    
    @property
    @abstractmethod
    def getSolve(self) -> any:
        """Returns the answer

        Returns:
            any: answer
        """
        ...

    @abstractmethod
    def __str__(self) -> any:
        """Returns string rep

        Returns:
            any: string rep
        """
        return str(self.solve)

    @abstractmethod
    def __repr__(self):
        """Returns string rep

        Returns:
            _type_: string rep
        """
        return self.__str__()

    def __len__(self):
        """Returns number of items in data

        Returns:
            any: number of items in data 
        """
        return len(self.data)

    def __getitem__(self, i):
        if isinstance(i, slice):
            return self.__class__(self.data[i])
        else:
            return self.data[i]

    def __setitem__(self, i, item):
        self.data[i] = item

    def __delitem__(self, i):
        del self.data[i]

    def append(self, item):
        self.data.append(item)

    def insert(self, i, item):
        self.data.insert(i, item)