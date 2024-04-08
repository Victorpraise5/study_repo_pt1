#!/usr/bin/python3
"""Square area module"""

class Square:
    """Square class"""

    def __init__(self, size=0):
        """initializes the data"""
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be na integer")

    def area(self):
        """calculates the area of square"""
        return self.__size ** 2
