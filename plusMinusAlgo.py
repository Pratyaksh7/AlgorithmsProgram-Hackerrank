size = int(input())

array = map(str, input().split())
positive = []
negative = []
zeros = []
for i in array:
    if int(i)>0 :
        positive.append(i)
    elif int(i) < 0:
        negative.append(i)
    else:
        zeros.append(i)
        
print("{: .6f}".format(len(positive)/size))
print("{: .6f}".format(len(negative)/size))   
print("{: .6f}".format(len(zeros)/size))  