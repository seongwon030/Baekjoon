n,m = map(int,input().split())
a = set()
b = set()
for i in range(n+m):
  k = input()
  if i<n:
    a.add(k)
  else:
    b.add(k)

t = sorted(a&b)
print(len(t))
for i in range(len(t)):
  print(t[i])