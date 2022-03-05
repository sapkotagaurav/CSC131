"""A Program to check if a given file contains the line of valid Magic Number Set

Author:Gaurab Sapkota
"""

def repeated(a): # Function to check if the numbers are repeated in a line
    nums = a.split()
    for a in range(len(nums)):
        for b in range(a+1,len(nums)):
            if nums[a]==nums[b]:
                return True
    return False

def make_matrix(line): # a function to take a line as a parameter and return a matrix
    temp = line.split()
    mat = list(map(lambda x: int(x),temp)) # lambda function used to convert string to integer
    matrix=[mat[0:3],mat[3:6],mat[6:9]]# taking each 3 digits to create row and 3 rows to create columns
    return matrix

def column_sum(matrix): # a function to check if the sum of columns is 15
    row = len(matrix)
    for index in range(len(matrix[0])):
        total =0
        for j in range(row):
            total = total + matrix[j][index]
        if total != 15:
            return False
    return True
        
def row_sum(m): # function to check if the sum of rows is 15
    for a in range(len(m)):
        if sum(m[a])!=15:
            return False
    return True
        
        
        
    

def main(): # main function to read file and pass to the function and display output
    file = open("input.txt","r")
    for line in file:
        matrix =make_matrix(line)
        repeated(line)
        # print valid if not repeated and sum=15 for both row and column, else print invalid
        print("valid") if(not repeated(line) and column_sum(matrix) and row_sum(matrix)) else print("invalid")
        
# calling the main function   
main()