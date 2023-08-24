from collections import deque
import sys

input = sys.stdin.readline

N,L = map(int,input().split())
A = list(map(int,input().split()))

re = []
k = deque()
for i in range(N):
  while k and k[-1][0] >= A[i]:
    k.pop()
  k.append((A[i],i))
  if k[0][1] <= i-L:
    k.popleft()
  print(k[0][0],end=' ')