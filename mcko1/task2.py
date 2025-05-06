arr = []

def f(n):
  n_bin = bin(n)[2:]
  m = ''
  if n % 4 == 0:
    m = '1'+n_bin+'10'
  else:
    m = n_bin+'01'
  return int(m, 2)
    
for i in range(100):
  if f(i) > 70:
    arr.append(i)

print(min(arr))        