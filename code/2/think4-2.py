import math

from swampy.TurtleWorld import *

# seperate arc with @n steps of polyline with each of the @step_length and turn @step_angle in each step
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

# move forward l@length then turn left @angle
def polyline(t, n, length, angle):
    for i in xrange(n):
        fd(t, length)
        lt(t, angle)

# draw one petal in flower
def petal(t, r, angle):
    for i in xrange(2):
        arc(t, r, angle)
        lt(t, 180 - angle)
 
# draw flower with n petal
def flower(t, n, r, angle):
    for i in xrange(n):
        petal(t, r, angle)
        lt(t, 360.0 / n)


#flower drawing

world = TurtleWorld()
flower_six = Turtle()
flower_six.delay = 0.0000001
flower(flower_six, 7, 100, 60)

world2 = TurtleWorld()
flower_ten = Turtle()
flower_ten.delay = 0.0000001
flower(flower_ten, 10, 100, 72)

world3 = TurtleWorld()
flower_twenty = Turtle()
flower_twenty.delay = 0.0000001
flower(flower_twenty, 20, 200, 18)

wait_for_user()