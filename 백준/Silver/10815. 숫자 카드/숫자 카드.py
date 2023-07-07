import sys

input = sys.stdin.readline

n = int(input())
k = set(map(int,input().split()))
m = int(input())
k1 = list(map(int,input().split()))

t = []
for i in range(len(k1)):
  a = set([k1[i]])
  a1 = k&a
  if not a1:
    t.append(0)
  else:
    t.append(1)

for i in range(len(t)):
  print(t[i],end=' ')