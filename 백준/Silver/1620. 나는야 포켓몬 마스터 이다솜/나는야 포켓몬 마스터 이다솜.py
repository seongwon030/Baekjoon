import sys

input = sys.stdin.readline

n,m = map(int,input().split())
hash = {}

for i in range(1,n+1):
  a = input().rstrip()
  hash[i] = a
  hash[a] = i

for j in range(m):
    c = input().rstrip()
    if c.isdigit():
      print(hash[int(c)])
    else:
      print(hash[c])