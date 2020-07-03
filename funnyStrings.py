def funnyString(string):
    stringlist = []
    for i in string:
        stringlist.append(ord(i))
        
    stringlist_rev = stringlist.copy()
    stringlist_rev.reverse()
    
    abs_diffs =[]
    rev_abs_diffs =[]
    
    for i in range(len(stringlist)):
        abs_diffs.append(abs(stringlist[i] - stringlist[i-1]))
        rev_abs_diffs.append(abs(stringlist_rev[i] - stringlist_rev[i-1]))
        
    if abs_diffs == rev_abs_diffs:
        print("Funny")
    else:
        print("Not Funny")
        

q = int(input())

for i in range(q):
    string = input()
    funnyString(string)