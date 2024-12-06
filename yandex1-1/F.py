data = input().split()
a1, b1 = int(data[0]), int(data[1])
a2, b2 = int(data[2]), int(data[3])

d1, d2 = 0, 0

if min(a1, b1) > max(a2, b2) or min(a2, b2) > max(a1, b1):
  if min(a1, b1) > max(a2, b2):
    d1 = max(a1, b1) + min(a2, b2)
    d2 = min(a1, b1)
  else:
    d1 = max(a2, b2) + min(a1, b1)
    d2 = min(a2, b2)
elif a1 == a2 or a1 == b2 or b1 == a2 or b1 == b2:
  if a1 == a2:
    d1 = a1
    d2 = b1 + b2
  if a1 == b2:
    d1 = a1
    d2 = a2 + b1
  if b1 == a2:
    d1 = a2
    d2 = a1 + b2
  if b1 == b2:
    d1 = b1
    d2 = a1 + a2
else:
  d1 = max(a1, b1, a2, b2)
  d2 = min(a1, b1) + min(a2, b2)

print(d1, d2)