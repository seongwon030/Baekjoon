n = int(input())
t = list(map(int, str(n)))
t.sort(reverse=True)
for i in range(len(t)):
  print(t[i],end='')