def designerPdfViewer(h, word):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_dict = dict(zip(list(alphabets), h))
    width = len(word)
    
    req_alphabets = []
    for i in alphabet_dict:
        if i in word:
            req_alphabets.append(i)
            
    req_alphabet_value =[]
    for i in req_alphabets:
        req_alphabet_value.append(alphabet_dict[i])
        
    print(width * max(req_alphabet_value))   

h = list(map(int, input().split()))
word = input()

designerPdfViewer(h, word)