import sys
input = sys.stdin.readline

def isprime(x):
    if x == 1:
        return False
    
    for i in range(2, int(x **(0.5))+1):
        if x % i == 0:
            return False
    return True

def dfs(x):
    if len(str(x)) == n:
        answer.append(x)
        return
    for i in range(1, 10, 2):
        if isprime(x*10+i):
            dfs(x*10+i)

n = int(input())
answer = []
dfs(2)
dfs(3)
dfs(5)
dfs(7)
print(*answer,sep="\n")