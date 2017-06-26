#This searches for character char in string aStr using bisection search and recursion

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized sorted string
    
    returns: True if char is in aStr; False otherwise
    '''
    low = 0 
    high = len(aStr) - 1 
    mid = (low + high) // 2
    if len(aStr) == 0:
        return False
    if len(aStr) < 3:
        if (char == aStr[0] or char == aStr[1]):
            return True
        else:
            return False
    if (char == aStr[mid]):
        return True
    elif (char > aStr[mid]):
        low = mid 
        aStr = aStr[low:(high + 1)] 
        return(isIn(char,aStr))
    elif (char < aStr[mid]):
        high = mid 
        aStr = aStr[low:(high + 1)] 
        return(isIn(char,aStr))
