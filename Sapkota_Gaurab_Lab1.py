
def getMatrix(numRows, numColumns):
    '''returns a matrix with the specified number of rows and columns'''
    m = []
    for row in range(numRows):
        r_ow = input("Enter {}X{} matrix for row {}: ".format(
            numRows, numColumns, row))
        f = r_ow.split(" ")
        x = []
        for a in f:
            x.append(float(a))
        m.append(x)
    return m


def display(twoD):
    for a in twoD:
        for b in a:
            print("%.2f"%(b), end=" ")
        print()


def sumColumn(twoD,col):
    numrows = len(twoD)
    su = 0

    for b in range(numrows):
        su = su + twoD[b][col]
    return su


def main():
    a = getMatrix(3, 4)
    print("The matrix is:\n")
    display(a)
    print("")
    for col in range(len(a[0])):
        print("The sum of elements in column %d is %.2f"% (col,sumColumn(a,col)))


main()
