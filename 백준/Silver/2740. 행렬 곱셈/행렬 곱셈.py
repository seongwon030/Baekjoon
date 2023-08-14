n,m = map(int,input().split()) 
A = [list(map(int,input().split())) for _ in range(n)]
m,k = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(m)]

C = list([0 for _ in range(k)] for _ in range(n))

for i in range(n):
    for j in range(k):
        for p in range(m):
            C[i][j]+=A[i][p]*B[p][j]

for r in C:
  print(*r)