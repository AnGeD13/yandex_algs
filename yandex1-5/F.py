n = int(input())
a = list(map(int, input().split()))
m = int(input())

a_sort = sorted(a)

obj = {}
for i in range(m):
  b, c = map(int, input().split())
  if b not in obj:
    obj[b] = c
  else:
    if obj[b] > c:
      obj[b] = c

sort_obj = sorted(obj.items(), key=lambda item: item[1])

R = 0
sum = 0
for i in range(n):
  while (a_sort[i] > sort_obj[R][0]):
    R += 1

  if (a_sort[i] <= sort_obj[R][0]):
    sum += sort_obj[R][1]

print(sum)