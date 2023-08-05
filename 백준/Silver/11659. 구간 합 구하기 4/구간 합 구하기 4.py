import sys

input = sys.stdin.readline

n,m = map(int,input().split())
k = list(map(int,input().split()))
k1 = [0]

cnt = 0
for i in range(len(k)):
  cnt+=k[i]
  k1.append(cnt)

for i in range(m):
  a,b = map(int,input().split())
  print(k1[b]-k1[a-1])