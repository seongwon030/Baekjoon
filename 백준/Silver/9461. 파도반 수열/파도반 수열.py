T = int(input())
d = [0] * 101
d[1],d[2],d[3] = 1,1,1
d[4],d[5] = 2,2

for _ in range(T):
  n = int(input())
  
  for i in range(6,n+1):
    if i <= 8:
      d[i] = d[i-1] +1
    elif 8 < i <= 10:
      d[i] = d[i-1] + 2
    else:
      d[i] = d[i-1] + d[i-5]
    
  print(d[n])