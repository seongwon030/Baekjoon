import sys

input = sys.stdin.readline

k = [0]*10001

T = int(input())
for i in range(T):
  k[int(input())] +=1 

for i in range(len(k)):
  if k[i]!=0:
    for j in range(k[i]):
      print(i)