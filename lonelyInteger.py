from collections import Counter
n = int(input())
a = [int(i) for i in input().split()]
c = Counter(a)
for val in c:
    if c[val] == 1:
        print(val)
        break
