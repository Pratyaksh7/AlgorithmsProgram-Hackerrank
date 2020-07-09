def extraLongFactorials(n):
    f = 1
    for i in range(n):
        f*= (i+1)
        
    print(f)    
        
n = int(input())

extraLongFactorials(n)
