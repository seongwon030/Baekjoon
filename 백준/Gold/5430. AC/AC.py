import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for i in range(T):
  hi = True
  er = 'y'
  a = list(input().strip())
  n = int(input())
  s = input().strip()[1:-1]
  if not s:
    if 'D' in a:
      er = 'error'
    else:
      er = 'y'
  else:
    s = deque((map(int,s.split(','))))
    for j in range(len(a)):
      if a[j]=='R':
        if hi:
          hi = False
        else:
          hi = True
      else:
        if not s:
          er = 'error'
        else:
          if hi:
            s.popleft()
          else:
            s.pop()

    if hi == False:
      s.reverse()
    else:
      s = s
  if er=='error':
    print(er)
  else:
    s = list(s)
    re = str(s).replace(" ", "")
    print(re)