n, k = map(int, input().split())
arr = input()

L, R = 0, 0
L_best, R_best = 0, 0
dist = 0
obj = {}
for i in range(n):
  if arr[i] not in obj: obj[arr[i]] = 1
  elif obj[arr[i]] < k: obj[arr[i]] += 1
  else:
    obj[arr[i]] += 1
    while obj[arr[i]] > k:
      obj[arr[L]] -= 1
      L += 1
  
  if dist < R - L:
    dist = R - L
    L_best, R_best = L, R

  R += 1

print(dist + 1, L_best + 1)