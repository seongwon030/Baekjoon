n,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

l = 0
r = n-1
last = 0
sum = 0
isLeft = False

for i in range(k):
  if isLeft:
    last = arr[l]
    l+=1
  else:
    sum += (arr[r] - last)
    r-=1
  isLeft = not isLeft
print(sum)