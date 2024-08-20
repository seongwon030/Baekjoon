import sys
input = sys.stdin.readline

m = int(input())

S = set()

for _ in range(m):
  k = input().split()
  if k[0] == 'add':
    if int(k[1]) not in S:
      S.add(int(k[1]))
  elif k[0] == 'remove':
    if int(k[1]) in S:
      S.remove(int(k[1]))
  elif k[0] == 'check':
    if int(k[1]) in S:
      print(1)
    else:
      print(0)
  elif k[0] == 'toggle':
    if int(k[1]) in S:
      S.remove(int(k[1]))
    else:
      S.add(int(k[1]))
  elif k[0] == 'all':
    S = set([i for i in range(1,21)])
  else:
    S = set()