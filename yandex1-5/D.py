n, r = map(int, input().split())
d_arr = list(map(int, input().split()))

k = 0
L, R = 0, 1

for i in range(L, n-1):
  for j in range(R, n):
    R = j
    if (d_arr[j] - d_arr[i] > r):
      k += n - j
      L += 1
      break

print(k)
