def hurdleRace(k, heights):
    # k is the height Dan can jump naturally
    Max_height = max(heights)
    num_of_potion = 0
    for i in heights:
        if k > i :
            num_of_potion = 0
        else:
            num_of_potion = Max_height - k
            
    print(num_of_potion)

n,k = map(int, input().split())

heights = list(map(int, input().split()))

hurdleRace(k, heights)