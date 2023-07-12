import sys

input = sys.stdin.readline

n,m = map(int,input().split())

a = set()
b = []

for i in range(n):
  k = input()
  a.add(k)

for j in range(m):
  k2 = input()
  b.append(k2)

cnt = 0
for i in range(len(b)):
  if b[i] in a:
    cnt += 1
print(cnt)