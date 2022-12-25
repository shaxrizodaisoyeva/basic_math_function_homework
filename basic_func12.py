def main(a):
    '''Round the value of a to 2 decimal places and return it.
    
    Args:
        a (float): a number
        
    Returns:
        float: the result
    '''
    a = round(a, 2)
    return a
a = 7.83487
print(main(a))