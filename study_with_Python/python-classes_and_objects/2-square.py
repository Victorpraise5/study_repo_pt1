#!/usr/bin/python3
"""Square Module"""

class Square:
    """Square class"""

    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >=o")
        else:
            raise TypeError("size must be an integer")
