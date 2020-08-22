t = int(input())
arr = [input() for _ in range(t)]
a = []
for i in arr:
    count = 0
    for j in i:
        if int(j) == 0:
            count += 0
        elif int(i) % int(j) == 0:
            count += 1
        else:
            count += 0
    a.append(count)

for i in a:
    print(i)
