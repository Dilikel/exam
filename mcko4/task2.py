arr = []

def f(n):
  n_bin = bin(n)[2:]
  m = ''
  if n % 4 == 0:
    m = '1' + n_bin + '10'
  else:
    m = '10' + n_bin + '1'
  return int(m, 2)

for i in range(1000):
  if f(i) > 90:
    arr.append(i)

print(min(arr))      