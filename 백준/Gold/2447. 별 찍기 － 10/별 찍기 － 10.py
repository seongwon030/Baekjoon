def do(n):
  if n==1:
    return ['*']

  st = do(n//3)
  k=[]

  for star in st:
    k.append(star*3)
  for star in st:
    k.append(star+' '*(n//3)+star)
  for star in st:
    k.append(star*3)

  return k

n=int(input())
print('\n'.join(do(n)))