# using python3

def MinDifference(n, arr):
    return (min(abs(x-y) for x, y in zip(arr, arr[1:])))


result = MinDifference(int(input()), sorted(map(int, input().split())))
print(result)
