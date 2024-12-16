strs, stolbs, mins = list(map(int, input().split()))
pole = []
mins_data = []
for i in range(strs+2):
  pole.append([0]*(stolbs+2))

for i in range(mins):
  data = input().split()
  x, y = int(data[0]), int(data[1])
  mins_data.append([x, y])
  pole[x-1][y-1] += 1
  pole[x-1][y] += 1
  pole[x-1][y+1] += 1
  pole[x][y-1] += 1
  pole[x][y+1] += 1
  pole[x+1][y-1] += 1
  pole[x+1][y] += 1
  pole[x+1][y+1] += 1

for i in range(len(mins_data)):
  x = mins_data[i][0]
  y = mins_data[i][1]

  pole[x][y] = '*'

for i in range(1, strs+1):
  s = ''
  for j in range(1, stolbs+1):
    s += str(pole[i][j]) + ' '
  print(s)
