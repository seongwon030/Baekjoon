s = input()

left = []
right = []
cnt = 0

for i in range(len(s)):
  if s[i] == '(':
    left.append('(')
  else: 
    if s[i-1] == ')':
      left.pop()
      cnt+=1
    else:
      left.pop()
      cnt += len(left)
print(cnt)