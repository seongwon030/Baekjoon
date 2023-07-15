import sys

input = sys.stdin.readline

T = int(input())
k=[]
for i in range(T):
  n = input().rstrip()
  if n[0] != '(' or n[-1] != ')':
    print("NO")
  else:
    for j in range(len(n)):
      if n[j]=='(':
        k.append(n[j])
      else:
        if not k:
          k.append(0)
          break
        else:
          k.pop()
    if not k:
      print("YES")
    else:
      print("NO")
  k.clear()