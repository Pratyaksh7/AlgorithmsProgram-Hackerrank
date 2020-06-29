def staircase(n):
    for i in range(1,n+1):
        print(str("#"*int(i)).rjust(n))


n = int(input())
staircase(n)