def miniMaxSum(arr):
   minsum = 0
   maxsum = 0
   for i in arr[0:len(arr)-1]:
       minsum += int(i)
   for j in arr[1:len(arr)]:
       maxsum += int(j)
   
   print("{} {}".format(minsum,maxsum))

arr = input().split()
arr.sort()
miniMaxSum(arr)