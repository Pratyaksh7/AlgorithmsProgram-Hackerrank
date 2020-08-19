def recursiveSum(numeric_string):

    # base case
    if len(numeric_string) == 1:
        return numeric_string

    # choice diagram
    else:
        l1 = [int(i) for i in numeric_string]
        return recursiveSum(str(sum(l1)))

n,k = list(map(str,input().split()))
k = int(k)
if k % 10 == 0:
    k = 1
numeric_string = n* k

print(recursiveSum(numeric_string))