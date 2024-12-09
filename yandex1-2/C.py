n = int(input())
data = input()
arr = [int(x) for x in data.split()]
result = int(input())

ans = 1001
raz = 3000
for i in range(n):
  if abs(arr[i] - result) < raz:
    raz = abs(arr[i] - result)
    ans = arr[i]

print(ans)

