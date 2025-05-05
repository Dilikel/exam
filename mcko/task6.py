alh = 'avens'
i = 0
arr = []

for x in alh:
  for y in alh:
    for z in alh:
      for w in alh:
        s = x+y+z+w
        i += 1
        if not 'e' in s and not 'aa' in s:
          arr.append(i)

print(min(arr))          