n = int(input())
ar = {}
values = list(map(int, input().split()))
k = int(input())
keys = list(map(int, input().split()))
for i in range(k):
  values[keys[i] - 1] -= 1

for i in range(n):
  if values[i] < 0:
    print("YES")
  else:
    print("NO")