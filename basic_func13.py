def main(a):
    '''find the square root of a number and return it.
    
    Args:
        a (int): a number
        
    Returns:
        float: the absolute value.
    ''' 
    from math import sqrt
    a = sqrt(a)
    a = abs(a)
    return a
a = 9
print(main(a))