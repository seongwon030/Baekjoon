def matrixmult(A,B):  # 행렬 곱 계산
    n = len(A)
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j]+=A[i][k]*B[k][j]
                C[i][j] = C[i][j]%1000
    return C

import sys

input = sys.stdin.readline

n,b = map(int,input().split())
A = []
for i in range(n):
  A.append(list(map(int,input().split())))

cn = []
while True:
  if b==1:
    break
  elif b%2==0: # 짝수
    b = b//2
    cn.append(1)
  else:
    b = (b-1)//2
    cn.append(0)

t = A
for i in range(len(cn)-1,-1,-1):
  if cn[i] == 1:
    A = matrixmult(A,A)
  else:
    C = matrixmult(A,A)
    A = matrixmult(t,C)

for i in range(len(A)):
  for j in range(len(A)):
    if j==len(A)-1:
      print(A[i][j]%1000, sep=' ')
    else:
      print(A[i][j]%1000,end=' ')