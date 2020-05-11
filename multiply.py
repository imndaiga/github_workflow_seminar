def multiply(float1, float2):
    """
    This function performs a multiplication between their two argument. 
    
    Parameters
    ----------
    float1: float number that will be the left part of the multiplication
    float2: float number that will be the right part of the multiplication
    
    Returns
    -------
    float
        
    Examples
    --------
    >>> multiply.multiply(5.4, 6.5)  
    35.1
    """
    
    if type(float1) != float or type(float2) != float:
        raise TypeError('Both arguments should be floats')
        
    return float1 * float2
