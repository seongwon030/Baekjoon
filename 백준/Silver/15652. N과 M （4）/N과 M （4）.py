n,m = map(int,input().split())

k = []

c=1
def re():
  global c

  if len(k) == m:
    print(' '.join(map(str,k)))
    return

  for i in range(c,n+1):
      k.append(i)
      c=max(k)
      re()  
      k.pop()
      

re()