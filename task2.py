# for x in range(2):
#     for y in range (2):
#         for z in range (2):
#             for w in range (2):
#                 f = (not (not w or y) or x ) or not z
#                 if f == 0:
#                     print(z, y, w, x, f)

# for x in range(2):
#  for y in range(2):
#   for z in range(2):
#     if not ((x or y) <= (y == z)):
#         print(x, y, z)

# def f1(x, y, z, w):
#     if (not x or y) == (w or  not z) == 1:
#         return 1
#     else:
#         return 0
#
# def f2(x, y, z, w):
#     if (not x or y) and (not w == z) == 1:
#         return 1
#     else:
#         return 0
#
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 print(x, z, y, w, '',  f1(x, z, y, w), '', f2(x, z, y, w))


# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = not (x == (not y)) or ((x and w) == (z and (not w)))
#                 if f == 0:
#                     print(w, z, y, x, f)


# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x and y) or (y and z)) == ((x <= w) and (w <= z)):
#                     print(x, y, z, w)

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f =  (x <= (z <= w)) and (z <= (y == (not w)))
#                 if f == 0:
#                     print(z, x, w, y, f)

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = (x <= (y == w)) and (y == (w <= z))
#                 if not f:
#                  print(y, x, w, z)


# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not ((not (y <= x)) or (z <= w) or (not z)):
#                     print(y,x,z,w)


# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (x or y) and (not (y == z) and (not w)):
#                     print(z, y, x, w)


# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 for u in range(2):
#                     if ((z <= w) and (y == (not x))) <= (u == (y or z)):
#                         print(w, y, z, x, u)