arr = list(map(int, input().split()))
min1 = 10**5
min2 = 10**5
max1 = -10**5
max2 = -10**5
max3 = -10**5
for i in range(len(arr)):
  if arr[i] < max(min1, min2):
    if min1 < arr[i] < min2:
      min2 = arr[i]
    else:
      min2 = min1
      min1 = arr[i]
  if arr[i] > min(max1, max2, max3):
    if arr[i] > max1:
      max3 = max2
      max2 = max1
      max1 = arr[i]
    elif arr[i] > max2:
      max3 = max2
      max2 = arr[i]
    elif arr[i] > max3:
      max3 = arr[i]

if min1 * min2 * max1 > max3 * max2 * max1:
  print(min1, min2, max1)
else:
  print(max3, max2, max1)
