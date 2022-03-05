""" Lab 3
Author:Gaurab Sapkota
"""

def stutter(aString:str):
    """A function to double every alphabet in a string

    Args:
        aString (str): original string
    """    
    if aString=="":
        return ""
    temp = aString[0]
    return temp*2+stutter(aString[1:])



    
def toNumber(aString:str):  
    """A function to return sum of all digits in a string

    Args:
        s (str): given string with digits

    """    
    if aString=="":
        return 0
    temp =aString[0]
    temp2=0
    if temp.isnumeric():
        temp2 = int(temp)
    return temp2 + toNumber(aString[1:])
    
    
    
        
def findMax(aList:list):
    """Function to find maximum number in given list

    Args:
        l (list): list of integers

    """    
    if len(aList)==1:
        return aList[0]
    return aList[0] if aList[0]>findMax(aList[1:]) else findMax(aList[1:])




def findAverage(aList:list):
    """Function to find average of given integers in a list

    Args:
        l (list): list of numbers

    """    
    if len(aList)==1:
        return aList[0]
    return (aList[0] + findAverage(aList[1:])*(len(aList)-1))/len(aList)


    
        
    
def main():
    print(stutter("adskj"))
    print(toNumber("G4ur4vs4pk014"))
    print(findMax([1,2,3,4,3,2,1]))
    print(findAverage([1,2,3]))
    
main()