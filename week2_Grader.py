import math

def polysum(n, s):
    """
    Input: n - Number of sides of a normal polygon
           s - length of each side
    Output: Sum of area and Perimeter squared
    Note: Perimeter = n*s
          Area = ( 0.25 * n * s^2 / tan( pi / n ) )
    """
    area = 0.25*n*s**2 / math.tan(math.pi/n)  # area according to formula
    perim  = n*s                              # perimeter
    su = area + perim**2                      # Output
    return round(su, 4)
