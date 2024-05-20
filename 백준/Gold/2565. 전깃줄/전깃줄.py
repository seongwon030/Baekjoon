n = int(input())
k = []
dp = [1]*n

for i in range(n):
  a,b = map(int,input().split())
  k.append([a,b])

k.sort()

for i in range(1,n):
  for j in range(0,i):
    if k[i][1] >= k[j][1]: 
      dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))