s1 = input()
s2 = input()

ar1 = []
ar2 = set()
k = 0

for i in range(len(s1)-1):
  ar1.append(s1[i: i+2])

for i in range(len(s2)-1):
  ar2.add(s2[i: i+2])

for gen in ar1:
  if gen in ar2:
    k += 1

print(k)