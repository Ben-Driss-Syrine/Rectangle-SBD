import pytest
from rectangle import Rectangle
from point import Point




@pytest.fixture(scope='class')
def lower_left_tester():
    return Point(4, 5)


@pytest.fixture(scope='class')
def rectangle_tester(lower_left_tester):
    return Rectangle(6, 4, lower_left_tester)


@pytest.fixture(scope='class')
def rectangle_issquare_tester(lower_left_tester):
    return Rectangle(4, 4, lower_left_tester)


# testing perimeter ()->float
def test_perimeter(rectangle_tester):
    assert rectangle_tester.perimeter() == 20.0


# testing area()->float
def test_area(rectangle_tester):
    assert rectangle_tester.area() == 24.0


# testing is_square()->bool
def test_is_square(rectangle_tester, rectangle_issquare_tester):
    assert rectangle_tester.is_square() == False
    assert rectangle_issquare_tester.is_square() == True


# testing distance_from_origin()->float
# QUADRANT I
@pytest.fixture(scope='class')
def lower_left_quadrant1():
    return Point(4, 5)


@pytest.fixture(scope='class')
def rectangle_tester_quadrant1(lower_left_quadrant1):
    return Rectangle(6, 4, lower_left_quadrant1)


# QUADRANT II
@pytest.fixture(scope='class')
def lower_left_quadrant2():
    return Point(-3, 2)


@pytest.fixture(scope='class')
def lower_left_quadrant3():
    return Point(-4, -4)


@pytest.fixture(scope='class')
def lower_left_quadrant4():
    return Point(6, -8)


@pytest.fixture(scope='class')
def lower_left_xyaxis():
    return Point(0, 7)


def test_distance_from_origin(rectangle_tester_quadrant1, lower_left_quadrant2, lower_left_quadrant3,
                              lower_left_quadrant4, lower_left_xyaxis):
    # QUADRANT I
    assert rectangle_tester_quadrant1.distance_from_origin(4, 5) == 6
    # QUADRANT II
    assert rectangle_tester_quadrant1.distance_from_origin(-3, 2) == 5
    # QUADRANT III
    assert rectangle_tester_quadrant1.distance_from_origin(-4, -4) == 5
    # QUADRANT IV
    assert rectangle_tester_quadrant1.distance_from_origin(6, -8) == 5
    # X-Y AXIS
    assert rectangle_tester_quadrant1.distance_from_origin(0, 7) == 5
