def camelcase(s):
    words = 0
    for i in range(len(s)):
        while str.isupper(s[i]):
            words += 1
            break
        
    print(words+1)    

s = input()
camelcase(s)