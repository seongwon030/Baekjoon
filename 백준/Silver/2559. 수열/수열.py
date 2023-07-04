import sys

input = sys.stdin.readline

n,k = map(int,input().split())

a = list(map(int,input().split()))

b = []
cnt = 0
for i in range(n-k+1):
  if i == 0:
    for j in range(k):
      cnt += a[j]
    b.append(cnt)
    cnt -= a[i]
  else:
    cnt += a[i+k-1]
    b.append(cnt)
    cnt -= a[i]

print(max(b))
