n, k = map(int, input().split())
arr = list(map(int, input().split()))

L, R = 0, 0
count = 0
sum = 0
while R < n:
  if sum < k: sum += arr[R]

  while sum > k:
    sum -= arr[L]
    L += 1

  if sum == k:
    count += 1
    sum -= arr[L]
    L += 1

  R += 1

print(count)