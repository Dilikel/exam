for x in '0123456789ABC':
  a = f'241{x}3'
  b = f'2{x}025'
  res = int(a, 13) + int(b, 13)
  if res % 19 == 0:
    print(res // 19)
