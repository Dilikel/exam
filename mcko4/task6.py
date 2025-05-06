alh = 'аелпрь'
arr = []
i = 0
for x in alh:
  for y in alh:
    for z in alh:
      for w in alh:
        s = x+y+z+w
        i += 1
        if s.count('е')==1 and not 'аа' in s:
          arr.append(i)

print(min(arr))