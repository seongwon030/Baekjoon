import sys

input = sys.stdin.readline

n,m=map(int,input().split())
s=set()
k=[]
for i in range(n):
    s.add(input().rstrip())
    
for j in range(m):
    a=input().rstrip()
    if a in s:
        k.append(a)

k.sort()
print(len(k))
for x in k:
    print(x)