n, m = map(int, input().split())
A = set()
B = set()
for i in range(n):
  A.add(int(input()))

for i in range(m):
  B.add(int(input()))

common = A.intersection(B)
anns = A.difference(B)
borys = B.difference(A)

print(len(common))
print(*sorted(common))

print(len(anns))
print(*sorted(anns))

print(len(borys))
print(*sorted(borys))
