arr1 = set(list(map(int, input().split())))
arr2 = set(list(map(int, input().split())))
print(*sorted(list(arr1 & arr2)))