from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
k = deque()
for i in range(n):
  a = input().rstrip()
  a = a.split(' ')
  s = a[0]
  if s == 'push':
    k.append(int(a[1]))
  if s == 'pop':
    if not k:
      print(-1)
    else:
      print(k.popleft())
  if s == 'size':
    print(len(k))
  if s == 'empty':
    if not k:
      print(1)
    else:
      print(0)
  if s == 'front':
    if not k:
      print(-1)
    else:
      print(k[0])
  if s == 'back':
    if not k:
      print(-1)
    else:
      print(k[-1])