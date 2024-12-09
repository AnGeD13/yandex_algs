a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

min_k1 = min(a, b, c)
min_k2 = a + b + c - max(a, b, c) - min_k1

if (min_k1 <= d and min_k2 <= e) or (min_k1 <= e and min_k2 <= d):
  print("YES")
else:
  print("NO") 
