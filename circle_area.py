""" Empty module docstring """
import math as m

def circle_area():
    """ Find the area of a circle """
    radius = float(input('Radius: '))
    radius_sqr = m.pow(radius, 2)
    area = m.pi * (radius_sqr)
    return area

_area = circle_area()
print(_area)
