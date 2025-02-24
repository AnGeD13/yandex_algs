n, k = map(int, input().split())
arr = list(map(int, input().split()))

L, R = 0, 0
distance = 10**6
L_best, R_best = 0, 0
obj = {}
for i in range(1, k+1):
  obj[i] = 0

while R < n and distance + 1 > k:
  obj[arr[R]] += 1

  while obj[arr[L]] > 1:
    obj[arr[L]] -= 1
    L += 1

  if distance > R - L and all(obj.values()):
    distance = R - L
    L_best, R_best = L, R

  R += 1

print(L_best+1, R_best+1)