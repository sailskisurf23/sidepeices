"""Point and Triangle classes.
This module contains classes to represent points and triangles in
two-dimensional space.


For this exercise, you will be writing a Point class. Here's some code showing how you should be able to use your Point class:

p1 = Point(1, 2)
p2 = Point(4, 7)
print "Distance between points:", p1.dist(p2)
There is some starter code for you in point.py

Implement the code in point.py so that the tests pass when you run make point on the command line.

Implement a Triangle class which uses the Point class. You should have three methods:

-   __init__
-   perimeter: Use the dist method from the Point class!
-   area: If you don't know how to calculate this, check this out.


"""

from math import sqrt

class Point(object):
    """Represent a point in 2-dimensional space using x and y cooridnates."""

    def __init__(self, x, y):
        """Initialize a Point with the given x and y coordinate values.
        Parameters
        ----------
        x : float
        y : float
        """
        pass

    def __repr__(self):
        """Return a string representation of the current Point.
        Examples
        --------
        >>> repr(Point(7, 7))
        "Point(7, 7)"
        """
        pass


    def __eq__(self, other):
        """Return True if the coordinates of self and other are identical.
        Parameters
        ----------
        other : Point
        Examples
        --------
        >>> Point(1, 1) == Point(1, 1)
        True
        >>> Point(1, 1) == Point(3, -1)
        False
        """
        pass

    def __add__(self, other):
        """Return a new Point representing the sum of self and other.
        Parameters
        ----------
        other : Point
        Examples
        --------
        >>> Point(1, 1) + Point(2, 3)
        Point(3, 4)
        >>> Point(1, 1) + Point(-1, -1)
        Point(0, 0)
        """
        return

    def __sub__(self, other):
        """Return a new Point representing the difference of self and other.
        Parameters
        ----------
        other : Point
        Examples
        --------
        >>> Point(1, 1) - Point(2, 3)
        Point(-1, -2)
        >>> Point(1, 1) - Point(-1, -1)
        Point(2, 2)
        """
        pass

    def __mul__(self, scale_factor):
        """Return a new Point with coordinates multiplied by scale_factor.
        Returns
        -------
        length : float
        Examples
        --------
        >>> Point(1, 1) * 2
        Point(2, 2)
        >>> Point(-3, 5) * 3
        Point(-9, 15)
        >>> Point(-2, 4) * -1
        Point(2, -4)
        """
        pass

    def length(self):
        """Return the length of the vector from the origin to this Point.
        Use the Pythagorean Theorem.
        Returns
        -------
        length : float
        Examples
        --------
        >>> length(Point(3,4))
        5
        """
        pass

    def dist(self, other):
        """Return the distance between this point and the other point given.
        Use __sub__ and length to compute the distance.
        Parameters
        ----------
        other : Point
        Returns
        -------
        distance : float
        Examples
        --------
        >>> dist(Point(1,1), Point(4, 5))
        5
        """
        pass


'''
This class will take 3 Point objects and have two methods to calculate the area and perimeter. You will be able to use the methods of the Point class to do a lot of the work.
Example of running this in Ipython or jupyter notebook would be

In [1]: from point_soln import Point, Triangle

In [2]: p1 = Point(1,1)

In [3]: p2 = Point(2,2)

In [4]: p3 = Point(3,1)

In [5]: t = Triangle(p1,p2,p3)

In [6]: t.area()
Out[6]: 1.0

In [7]: t.perimeter()
Out[7]: 4.82842712474619
'''
class Triangle(object):
    """Represent a triangle in 2-dimensional space using three Points."""

    def __init__(self, v1, v2, v3):
        """Create a new Triangle with vertices (v1, v2, v3)."""
        pass

    def perimeter(self):
        """Return the perimeter of the Triangle."""
        pass

    def area(self):
        """Return the area of the Triangle"""
        pass
