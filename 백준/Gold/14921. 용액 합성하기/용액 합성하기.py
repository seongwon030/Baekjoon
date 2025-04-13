import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int,input().split())))

start, end = 0, n-1
min_sum = abs(arr[start] + arr[end])
final = [arr[start], arr[end]]

while start <end:
  left = arr[start]
  right = arr [end]
  sum = left + right

  if abs(sum) < min_sum:
    min_sum = abs(sum)
    final = [left, right]
    if min_sum == 0:
      break

  if sum < 0:
    start += 1
  else:
    end -= 1

print(final[0] + final[1])