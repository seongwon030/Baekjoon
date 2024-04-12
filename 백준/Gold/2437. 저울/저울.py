import sys
input = sys.stdin.readline

n = int(input())
k = list(map(int,input().split()))
k.sort()

re = 1

for i in k:
  if re < i:
    break
  re+=i
  
print(re)