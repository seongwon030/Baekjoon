import sys
input = sys.stdin.readline

m = ' ' + input().rstrip()
n = ' ' + input().rstrip()

len_dp = [[0] * len(n) for _ in range(len(m))]

for i in range(1, len(m)):
    for j in range(1, len(n)):
        if m[i] == n[j]:
            len_dp[i][j] = len_dp[i-1][j-1] + 1
        else:
            len_dp[i][j] = max(len_dp[i-1][j], len_dp[i][j-1])

i,j = len(m) - 1, len(n) -1
lcs = []

while i > 0 and j > 0:
    if m[i] == n[j]:
        lcs.append(m[i])
        i -= 1
        j -= 1
    elif len_dp[i-1][j] > len_dp[i][j-1]:
        i -= 1
    else:
        j -= 1

print(len(lcs))
if lcs:
    print(''.join(reversed(lcs)))