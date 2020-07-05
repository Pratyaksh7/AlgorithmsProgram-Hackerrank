def howManyGames(p, d, m, s):
    games = 0
    while s >= p:
        games += 1
        s = s-p              #decreasing the total money on aech purchase
        p = max(p-d,m)       # comparing the initial money and the minimum money
        
    print(games)    

p, d, m, s = map(int, input().split())

howManyGames(p, d, m, s) z