END = -2*10**9

const_flag = True
ascending_flag = True
weak_ascending_flag = True
descending_flag = True
weak_descending_flag = True

prev = int(input())

while True:
  data = int(input())
  if data == END:
    break
  if data == prev:
    if ascending_flag:
      ascending_flag = False
    if descending_flag:
      descending_flag = False
  if data > prev:
    if weak_descending_flag:
      weak_descending_flag = False
    if descending_flag:
      descending_flag = False
    if const_flag:
      const_flag = False
  if data < prev:
    if weak_ascending_flag:
      weak_ascending_flag = False
    if ascending_flag:
      ascending_flag = False
    if const_flag:
      const_flag = False
    
  prev = data
  

if const_flag:
  print("CONSTANT")
elif ascending_flag:
  print("ASCENDING")
elif weak_ascending_flag:
  print("WEAKLY ASCENDING")
elif descending_flag:
  print("DESCENDING")
elif weak_descending_flag:
  print("WEAKLY DESCENDING")
else:
  print("RANDOM")
