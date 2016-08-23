import random

@ok
def ok_gbt ( ) :
    """This function should fail with the current seed"""
    random.seed (15)
    val = ( 0.5 > random.random() )
    print "Gregory Timmons is " + ("cool" if val else "not cool");
    if( not val ) :
        raise NameError()
    
    

