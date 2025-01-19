n = int(input())
x = input()
if x == x[::-1]:
    print(0)
else:
    x = x.split()
    for i in range(1, n):
        check = x[i:]
        if check == check[::-1]:
            ans = x[:i][::-1]
            print(len(ans))
            print(*ans)
            break