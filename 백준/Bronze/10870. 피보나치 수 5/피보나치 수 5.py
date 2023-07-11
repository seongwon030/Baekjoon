n=int(input())

def pe(n):
  if n==0:
    return 0
  if n==1:
    return 1
  if n==2:
    return 1
  return pe(n-2)+pe(n-1)

print(pe(n))