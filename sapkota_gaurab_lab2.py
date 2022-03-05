'''
Lab2
Class:CSC131
Author:Gaurab Sapkota


'''

from functools import reduce

''' Main function '''
def main():
    a = list(range(1,11))
    
    ''' Map and lambda to generate list of cubed numbers'''
    m = list(map(lambda x: x**3,a))
    print(m)
    
    '''lambda and filter function to filter factors of 3'''
    f1 = list(filter(lambda x:x%3==0,a))
    print(f1)
    
    '''reduce function to concat all the numbers in a list'''
    r1 = reduce(lambda x,y : str(x)+str(y),a)
    print(r1)
    
    '''list comprehension'''
    m_2 = [ x**3 for x in a]
    print(m_2)
    
    f1_2 = [x for x in a if x%3==0]
    print(f1_2)
    
    cubed_factorOf3 = [ x**3 for x in a if x**3%3==0]
    print(cubed_factorOf3)
    
    
    data ={1: "one", 3: "three", 4: "four", 5: "five", 8: "eight", 10: "ten"}
    print(evenFilter(data))
    
    print(findMin(3,2))



def evenFilter(data:dict):
    """A function to return a number's name if the number is even

    Args:
        data (dict): Dictionary of numbers and their names

    Returns:
        [type]: list
    """    
    return [data[x] for x in data.keys() if x%2==0 ]


def findMin(x,y):
    """Function to return the minimum number between given two numbers

    """ 
    return x if x<y else  y
    
'''Calling the main function'''
main()