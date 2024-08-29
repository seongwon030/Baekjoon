import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())

def prime(n):
  for i in range(2,int(n/2+1)):
    if n%i == 0:
      return False
  return True


def DFS(number):
  if len(str(number)) == n:
    print(number)
  else:
    for i in range(1, 10):
      if i % 2==0:
        continue
      if prime(number*10+i):
        DFS(number*10+i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)