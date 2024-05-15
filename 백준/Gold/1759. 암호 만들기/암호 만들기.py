from itertools import combinations

L,C = map(int,input().split())

k = list(map(str,input().split()))
k.sort()

vowels = 'aeiou'

com = combinations(k,L)

for c in com:
  vowel_cnt = sum(1 for char in c if char in vowels)
  consonant_cnt = L - vowel_cnt
  if vowel_cnt>=1 and consonant_cnt>=2:
    print(''.join(c))