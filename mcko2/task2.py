arr = []

def f(n):
  n_bin = bin(n)[2:]
  m = ''
  if n % 4 == 0:
    m = '10'+n_bin+'1'
  else:
    m = '1'+n_bin+'10'
  return int(m, 2)
    
for i in range(100):
  if f(i) > 80:
    arr.append(i)

print(min(arr))        