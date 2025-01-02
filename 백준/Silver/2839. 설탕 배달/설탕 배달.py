n = int(input())

# 1. 5로 나누어지면 5를 뺌
# 2. 3으로 나누어지면 3을 뺌
cnt = 0 
while True:
  if n%5 == 0:
    n -= 5
    cnt += 1
  elif n%3 == 0:
    n-=3
    cnt+=1
  else:
    if n>=5:
      n-=5
      cnt+=1
    else:
      n-=3
      cnt+=1
      
  if n==0:
    break
  elif n<2:
    break

if n==0:
  print(cnt)
else:
  print(-1)