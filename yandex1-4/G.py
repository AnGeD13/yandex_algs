file = open("input.txt", "r", encoding='utf-8')
x = file.readlines()

dict = {}

for line in x:
  s = line.split()
  if s[0] == 'DEPOSIT':
    name, sum = s[1], int(s[2])
    if name in dict:
      dict[name] += sum
    else:
      dict[name] = sum
  elif s[0] == 'WITHDRAW':
    name, sum = s[1], int(s[2])
    if name in dict:
      dict[name] -= sum
    else:
      dict[name] = -sum
  elif s[0] == 'BALANCE':
    name = s[1]
    if name in dict:
      print(dict[name])
    else:
      print("ERROR")
  elif s[0] == 'TRANSFER':
    name1, name2, sum = s[1], s[2], int(s[3])
    if name1 in dict:
      dict[name1] -= sum
    else:
      dict[name1] = -sum
    
    if name2 in dict:
      dict[name2] += sum
    else:
      dict[name2] = sum

  elif s[0] == 'INCOME':
    p = int(s[1])
    for name in dict:
      if dict[name] > 0:
        dict[name] += int(dict[name] / 100 * p)
