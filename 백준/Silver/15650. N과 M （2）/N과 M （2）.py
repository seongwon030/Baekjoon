n,m = map(int,input().split())

k = []

c=1
def re():
  global c

  if len(k) == m:
    print(' '.join(map(str,k)))
    return

  for i in range(c,n+1):
    if i not in k:
      k.append(i)
      c+=1
      re()
      c=k[-1]
      k.pop()

re()