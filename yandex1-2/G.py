data = input()
arr = [int(x) for x in data.split()]

arr.sort()

max1 = arr[0]
max2 = arr[1]

max3 = arr[-1]
max4 = arr[-2]
if max1 * max2 < max3 * max4:
  print(min(max3, max4), max(max3, max4))
else:
  print(min(max1, max2), max(max1, max2))