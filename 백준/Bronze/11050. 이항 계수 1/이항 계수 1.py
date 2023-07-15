def fac(n):
    if(n > 1):
        return n * fac(n - 1)
    else:
        return 1

n,k = map(int,input().split())

print(int(fac(n)/(fac(k)*fac(n-k))))