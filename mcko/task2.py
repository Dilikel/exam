arr = []

def f (n):
  bin_n = bin(n)[2:]
  m = ''
  if n % 2 == 0:
    m = bin_n + '10'
  else:
    m = '1' + bin_n + '00'
  return int(m, 2)  

for i in range(100):
  if f(i) > 107:
    arr.append(i)

print(min(arr))    