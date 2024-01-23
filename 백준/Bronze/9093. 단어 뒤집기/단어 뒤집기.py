for _ in range(int(input())):
  s = input()
  reverse_name = ''
  k = []

  for c in s:
    if c == " ":
      k.append(reverse_name)
      reverse_name = ''
      continue
    reverse_name = c + reverse_name
  k.append(reverse_name)

  re = ' '.join(k)
  print(re)