currentData = input().split()
n = set(list(input()))
k = 0
for word in n:
  if word not in currentData:
    k += 1

print(k)