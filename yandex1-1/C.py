new_tel = input()
tel1 = input()
tel2 = input()
tel3 = input()

code = "495"
tels = [new_tel, tel1, tel2, tel3]

for i in range(len(tels)):
  tels[i] = tels[i].replace('-', '')
  tels[i] = tels[i].replace('(', '')
  tels[i] = tels[i].replace(')', '')
  tels[i] = tels[i].replace('+7', '8')

  if code not in tels[i]:
    tels[i] = '8' + code + tels[i]

  if i != 0:
    if tels[0] == tels[i]:
      print("YES")
    else:
      print("NO")
