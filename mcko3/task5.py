for x in range(2):
  for y in range(2):
    for z in range(2):
      for w in range(2):
        f = not(x) or z and (not(y) or (w and z))
        if f == 0:
          print(y,x,z,w)