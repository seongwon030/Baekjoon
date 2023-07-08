import sys

input = sys.stdin.readline

import heapq

n = int(input())
p=[]

for i in range(n):
  a = int(input())
  if a>0:
    heapq.heappush(p, a)
  else:
    if not p:
      print(0)
    else:
      print(heapq.heappop(p))