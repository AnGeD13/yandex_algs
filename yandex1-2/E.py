n = int(input())
ar = list(map(int, input().split()))
V = 0
maxLength = ar[0]
maxLengthPos = 0
for i in range(1, len(ar)-1):
  if (maxLength < ar[i]):
    maxLength = ar[i]
    maxLengthPos = i
    V = 0
  elif (ar[i] % 5 == 0 and ar[i] % 2 != 0 and ar[i+1] < ar[i]):
    if (maxLengthPos != i and maxLength >= ar[i] and V < ar[i]):
      V = ar[i]

ar_sorted = sorted(ar, reverse=True)
k = 0
if (V != 0):
  for i in range(len(ar_sorted)):
    if (V == ar_sorted[i]):
      k += 1
      break
    else:
      k += 1

print(k)
