import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

hash = {}
for i in a:
  if i in hash:
    hash[i] += 1
  else:
    hash[i] = 1

print(' '.join(str(hash[i]) if i in hash else '0' for i in b ))