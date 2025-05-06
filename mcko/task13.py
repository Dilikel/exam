f = open(r'C:\Users\vladi\OneDrive\Документы\work\Proga\Python\exam\mcko\13.txt').readlines()

m = [int(x) for x in f]

lim = min([x for x in m if x % 15 != 0])
res = []

for a,b in zip(m, m[1:]):
  if a % lim == 0 and b % lim == 0:
    res.append(a+b)

print(len(res), max(res))    