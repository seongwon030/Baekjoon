import sys
input = sys.stdin.readline

def matrix_chain(n,p):
    m = [[0] * (n+1) for _ in range(n+1)]

    for r in range(1,n):
        for i in range(1, n-r+1):
            j = i + r
            m[i][j] = m[i+1][j] + p[i-1] * p[i] * p[j]
            for k in range(i+1, j):
                cost = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                if m[i][j] > cost:
                    m[i][j] = cost

    return m[1][n]

n = int(input())
p = []

for _ in range(n):
    r,c = map(int, input().split())
    if not p:
        p.append(r)
    p.append(c)

print(matrix_chain(n,p))