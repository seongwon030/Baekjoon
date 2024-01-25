from collections import deque
import sys

input = sys.stdin.readline

re1 = list(input().strip('\n'))
re2 = deque()

m = int(input())
for _ in range(m):
  k = input().split()

  if k[0] == 'L' and re1:
    re2.appendleft(re1.pop())
  elif k[0] == 'D' and re2:
    re1.append(re2.popleft())
  elif k[0] == 'B' and re1:
    re1.pop()
  elif k[0] == 'P':
    re1.append(k[1])

for i in re1:
  print(i, end='')
for j in re2:
  print(j, end='')