#!/usr/bin/env python
"""
file: 11.py
date: Sun Aug  3 21:37:03 EDT 2014
from: Project Euler: http://projecteuler.net
auth: tls
purp: In the 20x20 grid below, four numbers along a diagonal line have been marked in red.
    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 ...26
    67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 ..... 63
    24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 ........ 78
    21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 ........... 14
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
    The product of these numbers is 26 x 63 x 78 x 14 = 1788696.
    What is the greatest product of four adjacent numbers in the same direction
    (up, down, left, right, or diagonally) in the 20x20 grid?
    Ans: 70600674 on Sun Aug  3 21:36:53 EDT 2014
"""
def xset_up_matrix():
    matrix= []
    row= "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08"
    row= to_int(row)
    matrix.append(row)
    row= "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00"
    row= to_int(row)
    matrix.append(row)
    row= "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65"
    row= to_int(row)
    matrix.append(row)
    row= "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91"
    row= to_int(row)
    matrix.append(row)
    row= "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80"
    row= to_int(row)
    matrix.append(row)
    row= "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50"
    row= to_int(row)
    matrix.append(row)
    row= "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70"
    row= to_int(row)
    matrix.append(row)
    row= "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21"
    row= to_int(row)
    matrix.append(row)
    row= "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72"
    row= to_int(row)
    matrix.append(row)
    row= "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95"
    row= to_int(row)
    matrix.append(row)
    row= "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92"
    row= to_int(row)
    matrix.append(row)
    row= "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57"
    row= to_int(row)
    matrix.append(row)
    row= "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58"
    row= to_int(row)
    matrix.append(row)
    row= "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40"
    row= to_int(row)
    matrix.append(row)
    row= "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66"
    row= to_int(row)
    matrix.append(row)
    row= "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69"
    row= to_int(row)
    matrix.append(row)
    row= "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36"
    row= to_int(row)
    matrix.append(row)
    row= "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16"
    row= to_int(row)
    matrix.append(row)
    row= "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54"
    row= to_int(row)
    matrix.append(row)
    row= "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
    row= to_int(row)
    matrix.append(row)
    return matrix

def to_int(row):
    row= row.split()
    for i in range(0, len(row)):
        row[i]= int(row[i])
    return row

def set_up_matrix():
    """
    First solve problem using a 5x5 matrix.
    1  9 3 4 5
    2 30 4 5 6
    3  8 4 5 7
    4  5 6 7 8
    5  6 7 8 9
    """
    matrix= []
    row= "1 9 3 4 5"
    row= to_int(row)
    matrix.append(row)
    row= "2 30 4 5 6"
    row= to_int(row)
    matrix.append(row)
    row= "3 8 5 6 7"
    row= to_int(row)
    matrix.append(row)
    row= "4 5 6 7 8"
    row= to_int(row)
    matrix.append(row)
    row= "5 6 7 8 9"
    row= to_int(row)
    matrix.append(row)
    return matrix

def product( iterable ):
    """
    Return the product of all the elements in the  list.
    """
    p= 1
    for n in iterable:
        p *= n
    return p

def maxinrow(row,span=2):
    """
    Return the maximum product of the series of elements span long.
    """
    maximum= 0
    offset= span - 1
    for i in range(0,len(row)-offset,1):
        print row[i:i+span]
        ans= product(row[i:i+span])
        maximum = ans if ans > maximum else maximum
    return maximum

def maxofrows(matrix,span=2):
    """
    Go through the rows from top to bottom and return the maximum.
    """
    maximum= 0
    for i in range(0,len(matrix)):
        ans= maxinrow(matrix[i],span)
        maximum = ans if ans > maximum else maximum
    return maximum

def maxdiagl2r(matrix,span=2):
    """
    Get ul to lr diag moving across top row.
    Then get ul to lr diag moving down left column.
    Return maximum product found.
    """
    print("start across columns")
    maximum= 0
    end= len(matrix)
    start= 0
    col = 0
    while not ((len(matrix) - start) < span):
        row= []
        for r in range(0,end):
            row.append(matrix[r][r+ col])
        #print "> ", row
        ans= maxinrow(row,span)
        maximum = ans if ans > maximum else maximum
        col += 1
        end -= 1
        start += 1
    print("start down rows")
    end= len(matrix)
    rowstep= 0  # start at row one even tho did it above
    col= 0
    start= 0
    for r in range(0,len(matrix)):
        print matrix[r]
    while not ((len(matrix) - start) < span):
        row= []
        col= 0
        for r in range(rowstep,end):
            #print("r= %d, col= %d, end= %d" % (r, col, end))
            row.append(matrix[r][col])
            col += 1
        print "> ", row
        ans= maxinrow(row,span)
        maximum = ans if ans > maximum else maximum
        rowstep += 1
        start += 1
    return maximum

def maxdiagr2l(matrix,span=2):
    """
    Get ur to ll diag moving backwards across top row.
    Then get ur to ll diag moving down right column.
    Return maximum product found.
    """
    print("start backwards across columns")
    maximum= 0
    end= len(matrix)
    start= 0
    col = len(matrix)- 1
    while not ((len(matrix) - start) < span):
        row= []
        for r in range(0,end):
            row.append(matrix[r][col-r])
        print "> ", row
        ans= maxinrow(row,span)
        maximum = ans if ans > maximum else maximum
        col -= 1
        end -= 1
        start += 1
    print("start down rows on right side")
    end= len(matrix)
    rowstep= 0  # start at row one even tho did it above
    col= len(matrix) - 1
    start= 0
    for r in range(0,len(matrix)):
        print matrix[r]
    while not ((len(matrix) - start) < span):
        row= []
        col= len(matrix) - 1
        for r in range(rowstep,end):
            #print("r= %d, col= %d, end= %d" % (r, col, end))
            row.append(matrix[r][col])
            col -= 1
        print "> ", row
        ans= maxinrow(row,span)
        maximum = ans if ans > maximum else maximum
        rowstep += 1
        start += 1
    return maximum

def main():
    """
    """
    span= 4
    matrix= xset_up_matrix()
    print matrix
    maximum= 0
    ans= maxofrows(matrix,span)
    maximum = ans if ans > maximum else maximum
    print maximum   # maximum value along the rows
    # transpose columns to rows and call maxofrows again
    matrixT= zip(matrix[0],matrix[1],matrix[2],matrix[3],matrix[4])
    ans= maxofrows(matrixT,span)
    maximum = ans if ans > maximum else maximum
    # now work on going diagonally from upper left to lower  right
    ans= maxdiagl2r(matrix,span)
    maximum = ans if ans > maximum else maximum
    # Now go from upper right to lower left getting rows looking for maximum.
    ans= maxdiagr2l(matrix,span)
    maximum = ans if ans > maximum else maximum
    print("Maximum= %d" %  maximum)
    return 0

if __name__ == "__main__":
    main()
