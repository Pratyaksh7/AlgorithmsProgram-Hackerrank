# Project Euler #6: Sum square difference

cases = [int(input()) for i in range(int(input()))]
for i in cases:
    sums = ((i*(i+1))/2) ** 2
    squares = (i*(i+1)*((2*i)+1))/6
    print(int(sums - squares))



