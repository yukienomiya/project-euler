""" 
PROBLEM 28
Given an integer n, find the sum of the numbers placed on the two diagonals of the matrix (or spiral) 
n*n. The matrix/spiral is formed starting with the number 1 and moving to the right in a clockwise 
direction.

example:
n = 5
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

The output should be the sum of 25, 21, 17, 13, 9, 7, 5, 3, 1. The answer is therefore 101. 
"""



def es(num):
  lastNum = num * num
  somma = lastNum
  if (lastNum % 2 == 0):
    x1 = lastNum - (num - 1)
    x2 = x1 - num
    somma = x1 + x2
    lastNum = x2
    num -= 1
  while lastNum > 1:
    for idx in range(4):
      lastNum -= (num - 1)
      somma += lastNum
    num -= 2
  return somma