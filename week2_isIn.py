def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    index = len(aStr)//2
    # base case
    if len(aStr) <= 1:
        return False
    elif char == aStr[index]:
        return True
    # recursion
    elif char < aStr[index]:
        return isIn(char, aStr[:index])
    else:
        return isIn(char, aStr[index:])
print(isIn("a", "abcdefg"))
print(isIn("b", "abcdefg"))
print(isIn("c", "abcdefg"))
print(isIn("d", "abcdefg"))
print(isIn("e", "abcdefg"))
print(isIn("f", "abcdefg"))
print(isIn("g", "abcdefg"))
print(isIn("h", "abcdefg"))
print(isIn("m", "abcdefg"))
print(isIn("n", "abcdefg"))
print(isIn("n", ""))