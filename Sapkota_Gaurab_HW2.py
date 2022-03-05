'''
Jump it game using recursion
Author:Gaurab Sapkota

'''





def least_cost(aList:list):
    """ function to find the least cost of each board

    Args:
        aList (list): list of integers

    Returns:
        int: cost
    """    
    if len(aList)==1:
        return aList[0]
    if len(aList)==2:
        return aList[0]+ aList[1]
    if len(aList)==3:
        return aList[0]+aList[2]
    
    cost_jump = aList[0]+least_cost(aList[2:])
    cost_adjacent = aList[0]+least_cost(aList[1:])
    return min(cost_adjacent,cost_jump)

    

def read_file(filename):
    """function to read the lines of a file and return a 2d list of integers

    Args:
        filename (str): the name of file to read

    Returns:
        list: 2D list of integers
    """    
    integers =[]
    file = open(filename)
    
    for lines in file.readlines():
        integers.append([int(x)  for x in lines.strip().split(" ")]) #using strip function to remove whitespaces
    print(integers)
    return integers

def main():
    """ Calling the functions above to execute
    """    
    for i in read_file("input.txt"):
        print(least_cost(i))
    

main() #initiating the execution

'''
input sample: input.txt

0 5 75 7 43 11
0 3 80 6 57 10 
0 98 7 44 25 3 5 85 46 4 
0 57 59 83 9 42 70 
0 20 49 96 53 7 43 77 
0 24 17 15 61 49 61 8 65 43 26 99 7 57 97 50 93 6 82 52


output:
23
19
87
138
186
330





'''
        