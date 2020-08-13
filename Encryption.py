import math
s = input()
length = len(s)
rows = math.floor(math.sqrt(length))
columns = math.ceil(math.sqrt(length))
list1 = []
string = ""
for i in range(columns):
    string = ""
    for j in range(i, length, columns):
        string += s[j]
    list1.append(string)

for i in list1:
    print(i, end=" ")

