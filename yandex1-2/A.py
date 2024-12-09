data = input()
arr = [int(x) for x in data.split()]
flag = True
for i in range(1, len(arr)):
  if arr[i] <= arr[i-1]:
    print("NO")
    flag = False
    break
  
if flag:
  print("YES")