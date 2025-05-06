arr = []

for d in range(92):
  if (d * 13) % 20 == 1:
    arr.append(d)

print(max(arr))