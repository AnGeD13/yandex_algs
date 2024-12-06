string1 = input().split()
mode = input()

t_room, t_cond = int(string1[0]), int(string1[1])
match mode:
  case "freeze":
    if t_room > t_cond:
      print(t_cond)
    else:
      print(t_room)
  case "heat":
    if t_room < t_cond:
      print(t_cond)
    else:
      print(t_room)
  case "auto":
    print(t_cond)
  case "fan":
    print(t_room)


