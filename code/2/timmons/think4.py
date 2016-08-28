from swampy.TurtleWorld import *
import math

    
def petal( turtle, petal_length, petal_width) :

    radius =(
       ( float(petal_width) / 2.0) 
       +( ( float(petal_length) * float(petal_length)) / (8.0 * float( petal_width) ))
    )

    angle = math.degrees(
       2.0 * math.acos( 1.0 - ( float(petal_width) / float(radius) ) )
    )
    
    arclen = (float(angle) / 180.0) * math.pi * radius

    print( radius, angle, arclen )

    n = int( arclen / 3 ) + 1
    step_len = arclen / n
    step_ang = angle / n
    for i in xrange( 2 ) :
        for i in xrange( n ) :
            turtle.fd( step_len )
            turtle.lt( step_ang )
        turtle.lt( 180.0 -  angle )
    
def flower( turtle, petal_count, petal_length, petal_width ) :
    petal_angle = 360.0 / float(petal_count)

    for i in xrange( petal_count ) :
        petal( turtle, petal_length, petal_width )
        turtle.lt( petal_angle )
    

def square_flower( turtle, petal_count, petal_length ) :

    petal_angle = 360.0 / float(petal_count)
    inner_angle = (90.0 - float(petal_angle) / 2.0) 
    bar_length  = 2.0 * float(petal_length) * (math.sin( math.radians( float(petal_angle)) / 2 ))

    print( petal_angle, inner_angle)
    for i in xrange(petal_count) :
        turtle.fd( petal_length )
        turtle.lt( 180 - inner_angle  ) 
        turtle.fd( bar_length   ) 
        turtle.lt( 180 - inner_angle  ) 
        turtle.fd( petal_length )
        turtle.lt( 180 )
    
world = TurtleWorld()
billy = Turtle()
billy.set_delay(0.00001)

square_flower(billy,10, 100)

world.mainloop()
