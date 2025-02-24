n = int(input())
max_arr = [0]*n
min_arr = [0]*n

x_prev, y_prev = map(int, input().split())

for i in range(n-1):
  x_next, y_next = map(int, input().split())
  if y_next >= y_prev:
    max_arr[i+1] = y_next - y_prev + max_arr[i]
    min_arr[i+1] = min_arr[i]
  elif y_prev > y_next:
    min_arr[i+1] = y_prev - y_next + min_arr[i]
    max_arr[i+1] = max_arr[i]
  x_prev, y_prev = x_next, y_next

m = int(input())
for i in range(m):
  start, end = map(int, input().split())
  if start < end:
    print(max_arr[end-1] - max_arr[start-1])
  else:
    print(min_arr[start-1] - min_arr[end-1])
