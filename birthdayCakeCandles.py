def birthdayCakeCandles(heights):
    heights = list(heights)
    print(heights.count(max(heights)))
      

n = int(input())

heights = map(int, input().split())

birthdayCakeCandles(heights)