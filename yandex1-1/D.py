a = int(input())
b = int(input())
c = int(input())

no_solution = "NO SOLUTION"
many_solutions = "MANY SOLUTIONS"

if c < 0:
  print(no_solution)
else:
  if a == 0:
    if c**2-b == 0:
      print(many_solutions)
    else:
      print(no_solution)
  if a != 0:
    x = (c**2-b)/a
    if int(x) == x:
      print(int(x))
    else:
      print(no_solution)
    