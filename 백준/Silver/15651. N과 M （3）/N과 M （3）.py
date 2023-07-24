n,m = map(int,input().split())

k = []

def re():
 
  if len(k) == m:
    print(' '.join(map(str,k)))
    return

  for i in range(1,n+1):
      k.append(i)
      re()
      k.pop()

re()