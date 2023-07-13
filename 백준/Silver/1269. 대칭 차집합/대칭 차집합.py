import sys

input = sys.stdin.readline

n,m = map(int,input().split())

a = set()
b = set()

k = list(map(int,input().split()))
k2 = list(map(int,input().split()))

for i in range(len(k)):
  a.add(k[i])
for j in range(len(k2)):
  b.add(k2[j])

re = (a-(a&b)) | (b-(a&b))
print(len(re))