from point import Point
import math


class Rectangle(Point):
    """
    TO-DO:
    attributes
    lower_left :Point
    length :float
    width :float

    __init__
    attributes to properties
    methods
    area()->float
    perimeter()->float
    is_square()->bool
    distance_from_origin()->float
        (start with distance of lower_left to origin. how would you change to find distance of *closest point* to origin?)
        how would you TEST this method?
    """

    def __init__(self, length: float, width: float, lower_left):

        self._lower_left = None
        self._length = None
        self._width = None

        self.length = length
        self.width = width



        self.lower_left = lower_left



        # Property Construction

    # Length Property :
    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    @length.deleter
    def length(self):
        del self._length

    # Width Property :
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @width.deleter
    def width(self):
        del self._width

    # Lower Left Property :
    @property
    def lower_left(self):
        return self._lower_left

    @lower_left.setter
    def lower_left(self, lower_left):
        self._lower_left = lower_left

    @lower_left.deleter
    def lower_left(self):
        del self._lower_left

    def __str__(self):
        return f"Rectangle : Length= {self.length}, Width = {self.width}, Lower_left = {self.lower_left}"

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * (self._length + self._width)

    def is_square(self):
        if self._length == self._width:
            return True
        else:
            return False

    def distance_from_origin(self,x,y):
        """

                1.  Lower_left is going to determine where rectangle is located ( Quadrant 1/2/3/4 ) or,
                in the x or y-axis
                2.  try to imagine that we're projecting a tiny right rectangle that connects the closest point to
                the origin by the hypotenuse
                3. we calculate the hypotenuse using cosine/sine identities
                4. and  we have the closest  distance to the origin


         """
        # Quadrant II :

        if x < 0 and y > 0:

            return round(abs((Point.distance_from_origin(self._lower_left) - self._width) / math.cos(45)))

        # Quadrant III :
        elif x < 0 and y < 0:
            return round(abs((Point.distance_from_origin(self._lower_left) - self._width) / math.cos(45)))

        # Quadrant IV :
        elif x > 0 and y < 0:
            return round(abs((Point.distance_from_origin(self._lower_left) - self._width) / math.cos(45)))

        # If the rectangle intersects with x/y axis
        elif x == 0 or y == 0:
            return round(abs((Point.distance_from_origin(self._lower_left) * math.sin(45))))
        # Quadrant I
        else:
            return round(Point.distance_from_origin(self._lower_left))




