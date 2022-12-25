def main(a, b):
    '''find the absolute value of the difference between a and b. Return it.
    
    Args:
        a (int): a number
        b (int): a number
        
    Returns:
        int: the result.
    '''
    result = a-b
    result = abs(result)
    return result
a = 89
b = 679
print(main(a, b))