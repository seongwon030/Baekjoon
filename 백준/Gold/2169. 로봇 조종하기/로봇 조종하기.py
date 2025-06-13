import sys, copy
input = sys.stdin.readline

n,m = map(int, input().split())
robot = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

dp[0] = copy.deepcopy(robot[0])
for i in range(1, m):
    dp[0][i] += dp[0][i-1]

for i in range(1,n):
    left = [0] * m
    right = [0] * m

    for j in range(m):
        if j == 0:
            left[j] = robot[i][j] + dp[i-1][j]
            right[m-1-j] = robot[i][m-1-j] + dp[i-1][m-1-j]
            continue

        left[j] = robot[i][j] + max(dp[i-1][j], left[j-1])
        right[m-1-j] = robot[i][m-1-j] + max(dp[i-1][m-1-j], right[m-j])

    temp = [max(left[i], right[i]) for i in range(m)]
    dp[i] = copy.deepcopy(temp)

print(dp[n-1][m-1])