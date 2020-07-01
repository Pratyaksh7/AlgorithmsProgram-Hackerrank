def bigSorting(unsorted):
    unsorted.sort(key=int)
    for i in unsorted:
        print(i)

n = input()

unsorted = []

for _ in range(int(n)):
    item = input()
    unsorted.append(item)
    
bigSorting(unsorted)

