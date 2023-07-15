import sys

input = sys.stdin.readline

m = 1000000
k = [False,False] + [True]*(m-1)  # 0과 1은 제외

for i in range(2,m+1):
  if k[i]:
    for j in range(2*i,m+1,i):  # 배수를 계속 없애는 에라토스테네스의 체
      k[j] = False

T = int(input())
for x in range(T):
  cnt = 0
  n = int(input())
  for i in range(2,n//2+1): 
    if k[i] and k[n-i]:
      cnt+=1
  print(cnt)