n = int(input())
s = list(map(int, input().split()))
d, m = map(int, input().split())
count = 0
for i in range(len(s)-m+1):
    if sum(s[i:m+i]) == d:
        count += 1

print(count)
