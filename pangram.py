def pangrams(s):
    final = []
    spaces = []
    for i in set(s):
        if str.isspace(i):
            spaces.append(i)
        else:
            final.append(i)
            
    if len(final) == 26:
        print("pangram")
    else:
        print("not pangram")
          
    
s = input().lower()

pangrams(s) 