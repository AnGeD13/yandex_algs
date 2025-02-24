n, k = map(int, input().split())
n_arr = list(map(int, input().split()))
k_arr = list(map(int, input().split()))

for i in range(k):
  test = k_arr[i]
  if test >= n_arr[n-1]: print(n_arr[n-1])
  elif test <= n_arr[0]: print(n_arr[0])
  else:
    L, R = 0, n-1

    while R - L > 1:
      m = (L + R + 1)//2
      if (n_arr[m] <= test):
        L = m
      else:
        R = m

    if abs(test - n_arr[L]) <= abs(test - n_arr[R]):
      print(n_arr[L])
    else: print(n_arr[R])
  