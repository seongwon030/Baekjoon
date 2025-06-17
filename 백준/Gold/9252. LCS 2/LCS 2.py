import sys
input = sys.stdin.readline

m = ' ' + input().rstrip()
n = ' ' + input().rstrip()

string_dp = [[''] * len(n) for _ in range(len(m))]

for i in range(1, len(m)):
    for j in range(1, len(n)):
        if m[i] == n[j]:
            string_dp[i][j] = string_dp[i-1][j-1] + m[i]
        else:
            if len(string_dp[i][j-1]) > len(string_dp[i-1][j]):
                string_dp[i][j] = string_dp[i][j-1]
            else:
                string_dp[i][j] = string_dp[i-1][j]

print(len(string_dp[-1][-1]))
if len(string_dp[-1][-1]) > 0:
    print(string_dp[-1][-1])