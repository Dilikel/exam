for x in '0123456789AB':
  a = f'154{x}3'
  b = f'1{x}365'
  res = int(a, 12) + int(b, 12)
  if res % 13 == 0:
    print(x, res // 13)