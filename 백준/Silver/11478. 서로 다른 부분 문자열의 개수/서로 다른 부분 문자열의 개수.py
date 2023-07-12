s = input()

k = set()

for i in range(len(s)):
  for j in range(i+1, len(s)+1):
    k.add(s[i:j])
print(len(k))