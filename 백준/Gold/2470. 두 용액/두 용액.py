import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int,input().split())))

start, end = 0, n-1
min_sum = abs(arr[start] + arr[end])
ans = [arr[start], arr[end]]

if arr[start] >= 0:
    print(arr[start], arr[start+1])
    sys.exit()
elif arr[end] <=0:
    print(arr[end-1],arr[end])
    sys.exit()
else:
  while start < end:
      left = arr[start]
      right = arr[end]

      sum = left + right
      if (abs(sum)) < min_sum:
          min_sum = abs(sum)
          ans = [left, right]
          if ans == 0:
              break
      
      if sum < 0:
          start += 1
      else:
          end -= 1
  print(ans[0], ans[1])