#!/usr/bin/python3
"""Square Module"""

class Square:
    """Square class"""

    def __init__(self, size=0):
        """initializing data"""
        self.size = size

    @property
    def size(self):
        """Retunrs the size of the square instance """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of a square instance"""
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Calculates the Square's area"""
        return self.__size ** 2
