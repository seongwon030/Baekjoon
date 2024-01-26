from collections import deque
import sys

input = sys.stdin.readline

re = deque([])

n = int(input())
for i in range(n):
  k = input().split()
  if k[0] == 'push':
    re.append(k[1])
  elif k[0] == 'pop':
    if not re:
      print(-1)
    else:
      print(re.popleft())
  elif k[0] == 'size':
    print(len(re))
  elif k[0] == 'empty':
    if not re:
      print(1)
    else:
      print(0)
  elif k[0] == 'front':
    if not re:
      print(-1)
    else:
      print(re[0])
  elif k[0] == 'back':
    if not re:
      print(-1)
    else:
      print(re[-1])