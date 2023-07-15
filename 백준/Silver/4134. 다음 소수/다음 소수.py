import sys

input = sys.stdin.readline

import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

T = int(input())
for i in range(T):
  n = int(input())
  if n==0 or n==1:
    print(2)
  else:
    while True:
      if is_prime_number(n):
        print(n)
        break
      else:
        n+=1