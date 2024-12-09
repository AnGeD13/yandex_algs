a = int(input())
b = int(input())
n = int(input())
m = int(input())

min_a = n + a * (n - 1)
max_a = min_a + 2 * a

min_b = m + b * (m - 1)
max_b = min_b + 2 * b

if max(min_a, min_b) > min(max_a, max_b):
  print(-1)
else:
  print(max(min_a, min_b), min(max_a, max_b))