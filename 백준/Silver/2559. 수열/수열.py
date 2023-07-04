import sys

input = sys.stdin.readline

n,k = map(int,input().split())

a = list(map(int,input().split()))

re = []

re.append(sum(a[:k]))

for i in range(n-k):
  re.append(re[i] - a[i] + a[k+i])

print(max(re))