import sys
input = sys.stdin.readline

m = ' ' + input().rstrip()
n = ' ' + input().rstrip()

dp = [[0] * len(n) for _ in range(len(m))]

for i in range(1, len(m)):
    for j in range(1, len(n)):
        if m[i] == n[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])