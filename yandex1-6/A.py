n, k = map(int, input().split())
n_arr = list(map(int, input().split()))
k_arr = list(map(int, input().split()))

for i in range(k):
  L, R = 0, n-1
  while L < R:
    m = (L+R)//2
    if (n_arr[m] >= k_arr[i]):
      R = m
    else:
      L = m + 1

  if n_arr[L] == k_arr[i]: print("YES")
  else: print("NO")