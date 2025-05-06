arr = []

for d in range(92):
  if (d * 19) % 72 == 1:
    arr.append(d)

print(max(arr))