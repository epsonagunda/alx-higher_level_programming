#!/usr/bin/python3
"""
class rectangel that inherits from base
"""
from models.base import Base

class Rectangle(Base):
    """
    rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width.setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise valueError("width must be > 0 ")
        self.__width = value

    @property
    def height(self):
        """
        height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height.setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise valueError("height must be > 0 ")
        self.__height = value

    @property
    def x(self):
        """
        x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x.setter
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise valueError("x must be >= 0 ")
        self.__x = value

    @property
    def y(self):
        """
        y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y.setter
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise valueError("y must be >= 0 ")
        self.__y = value
