arr = []

def f(n):
  n_bin = bin(n)[2:]
  m = ''
  if n % 4 == 0:
    m = n_bin + '01'
  else:
    m = '1' + n_bin + '10'
  return int(m, 2)

for i in range(1000):
  if f(i) > 100:
    arr.append(i)

print(min(arr))