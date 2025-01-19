n = int(input())
ar_x = set()
for i in range(n):
  x, y = map(int, input().split())
  if x not in ar_x:
    ar_x.add(x)
  
print(len(ar_x))