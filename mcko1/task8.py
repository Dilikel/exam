arr = []

for d in range(120):
  if (d * 17) % 60 == 1:
    arr.append(d)

print(max(arr))