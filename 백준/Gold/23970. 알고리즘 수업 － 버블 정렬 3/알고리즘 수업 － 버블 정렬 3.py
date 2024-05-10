import sys
input = sys.stdin.readline

n = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

def bubble_sort(A,B):
  for i in range(len(A) - 1, 0, -1):
      for j in range(i):
          if A[j] > A[j + 1]:
              A[j], A[j + 1] = A[j + 1], A[j]
              if A[j+1] == B[j+1]:
                if A==B:
                  print(1)
                  sys.exit(0)
  print(0)

if A==B:
  print(1)
  sys.exit(0)
else:
  bubble_sort(A,B)