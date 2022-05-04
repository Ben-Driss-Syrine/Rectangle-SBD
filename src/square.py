from point import Point
from rectangle import Rectangle


class Square(Rectangle):
    """
    TO_DO
    __init__ -- how is it related to superclass __init__?
    do any methods need to be overridden?
    do the properties work?
    """

    def __init__(self, length, width, lower_left):
        Rectangle.__init__(self, length, width, lower_left)

    def __str__(self):
        Rectangle.__str__(self)
        return f"Square : Length= {self.length}, Width = {self.width}, Lower_left = {self.lower_left}"

    # Overriding Properties :

        # Length's Properties :

    @Rectangle.length.setter
    def length(self):
        return self._length

    @Rectangle.length.setter
    def length(self):
        return self._length

    @Rectangle.length.deleter
    def length(self):
        del self._length

        # Width Properties :

    @Rectangle.width.setter
    def width(self):
        return self._width

    @Rectangle.width.deleter
    def width(self):
        del self._width

        # lower_left Properties :

    @Rectangle.lower_left.setter
    def lower_left(self):
        return self._lower_left

    @Rectangle.lower_left.deleter
    def lower_left(self):
        del self._lower_left

    # Square Methods :

    def square_area(self):
        return self.length ** 2

    def square_perimeter(self):
        return self.length * 4


