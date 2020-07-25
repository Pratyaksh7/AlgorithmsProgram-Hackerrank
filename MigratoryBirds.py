n = int(input())
count = [0]*n
arr = map(int, input().split())
for i in arr:
    count[i] += 1
print(count.index(max(count)))
