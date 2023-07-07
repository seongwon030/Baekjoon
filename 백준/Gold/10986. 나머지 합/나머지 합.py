import sys

input = sys.stdin.readline

n,m = map(int,input().split())

a = list(map(int,input().split()))

sum = 0

k = [0] * m  

for i in range(n):
    sum += a[i]   
    k[sum%m] += 1

re = k[0] 

for i in range(len(k)):
    re += k[i]*(k[i]-1)//2  
print(re)
