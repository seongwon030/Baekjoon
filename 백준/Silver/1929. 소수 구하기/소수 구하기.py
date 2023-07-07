m,n = map(int, input().split())

a = [False,False] + [True]*(n-1)  # 0과 1은 제외
primes=[]
primes1=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i,n+1,i):
      a[j] = False

for i in range(2,m):
  if a[i]:
    primes1.append(i)
    for j in range(2*i,m,i):
      a[j] = False

p = set(primes)
p1 = set(primes1)
p2 = list(p-p1)
p2.sort()

for i in range(len(p2)):
  print(p2[i])