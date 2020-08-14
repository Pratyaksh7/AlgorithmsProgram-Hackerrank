# Multiples of 3 and 5

T = int(input())
arr = [int(input()) for i in range(T)]
results = []
for i in arr:
    sum = 0
    for j in range(i):
        if j%3 == 0 or j%5 ==0:
            sum += j
        else:
            continue
    results.append(sum)
for i in results:
    print(i)

