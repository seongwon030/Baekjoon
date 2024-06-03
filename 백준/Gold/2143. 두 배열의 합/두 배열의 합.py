import bisect
import sys

input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

A_sum, B_sum = [],[]
for i in range(n):
  for j in range(i+1,n+1):
    A_sum.append(sum(A[i:j]))
for i in range(m):
  for j in range(i+1,m+1):
    B_sum.append(sum(B[i:j]))

A_sum.sort()
B_sum.sort()

cnt = 0
for i in range(len(A_sum)):
  p = T - A_sum[i]
  left = bisect.bisect_left(B_sum,p)
  right = bisect.bisect_right(B_sum,p)
  cnt += (right - left)
print(cnt)