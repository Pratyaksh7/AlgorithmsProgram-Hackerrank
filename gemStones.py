def gemstones(arr):
    gems = set.intersection(arr[0],arr[1],arr[2])
    #gems = set.intersection(*arr) 
    #  *arr is used to get all the elements of the list arr when we are not known 
    #  how many elements will be present in any test case
    print(len(gems))

n = int(input())

arr = []
for _ in range(n):
    arr_item = input()
    arr.append(set(arr_item)) 
    
gemstones(arr)    