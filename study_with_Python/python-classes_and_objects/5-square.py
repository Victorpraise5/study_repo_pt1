#!/usr/bin/python3
"""Square module"""

class Square:
    """Square class"""

    def __init__(self, size=0):
        """initialization of data"""
        self.size = size

    @property
    def size(self):
        """returns the size of a square instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of a square instance"""
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print(" ")
        else:
            for i in range(self.__size):
                print(self.__size * "#")
