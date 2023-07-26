n = int(input())

cnt = 0
cnt1 = 0

def fi(n):
  
  global cnt
  if n==1 or n ==2:
    return 1
  else:
    cnt+=1
    return fi(n-2) + fi(n-1)


def pi(n):
  global cnt1
  f = [1,1]
  for i in range(2,n+1):
    f.append(f[-1] + f[-2])
    cnt1+=1
  return f[-1]

fi(n)
pi(n)
print(cnt+1,end=' ')
print(cnt1-1)