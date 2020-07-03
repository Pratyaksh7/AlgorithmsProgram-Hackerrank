def marsExploration(s):
    count = 0
    if len(s) %3 == 0:
        for i in s:
            if i != 'S' and i != 'O':
                count += 1
    else:
        return False
    
    print(count)

s = input().upper()

marsExploration(s)
