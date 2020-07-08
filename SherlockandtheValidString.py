from collections import Counter
def isValid(s):
    x = Counter(s)
    if len(set(x.values())) == 1:
        print("Yes")
    elif len(set(x.values())) > 2:
        print("No")
    else:
        Max = max(x.values())
        Min = min(x.values())
        
        if list(x.values()).count(Min) == 1:
            print("Yes")
        if list(x.values()).count(Max) > 1 or Max-Min > 1:
            print("No")   
        else:
            print("Yes")

s = input()

isValid(s)