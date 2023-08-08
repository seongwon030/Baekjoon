import sys

input = sys.stdin.readline

n = int(input())
dp = [list(map(int,input().split())) for _ in range(n)]

r = [[0 for _ in range(len(l))] for l in dp]

r[0][0] = dp[0][0]

for i in range(1,n):
  r[i][0] = r[i-1][0] + dp[i][0]
  r[i][-1] = r[i-1][-1] + dp[i][-1]
  for j in range(1,i):
    r[i][j] = max(r[i-1][j-1],r[i-1][j]) + dp[i][j]

print(max(r[-1]))