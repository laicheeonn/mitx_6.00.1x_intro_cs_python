

# Page 85

def sumDigits(s):

    """
    Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5
    """ 

    assert type(s) == str, "Argument is not a string"
    sumDigit = 0
    for i in range(len(s)):
        try:
            sumDigit += int(s[i])
        except ValueError:
            continue
    return sumDigit



# Page 88

def findAnEven(l):     
    
    """
    Assumes l is a list of integers
    Returns the first even number in l
    Raises ValueError if l does not contain an even number
    """ 
    
    assert all(type(num) in (float, int) for num in l), "Argument must be integers"
    assert len(l) != 0, "Argument cannot be empty list"
       
    try:
        isEven = [num % 2 == 0 for num in l]
        if sum(isEven) == 0:
            raise ValueError("l does not contain an even number")
        else:
            return l[isEven.index(True)]            
    except ValueError, msg:   
        print(msg)
         
    



        
