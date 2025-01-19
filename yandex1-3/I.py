n = int(input())
all = {}
for i in range(n):
  m = int(input())
  for i in range(m):
    language = input()
    if language not in all:
      all[language] = 1
    else:
      all[language] += 1

known = set()
others = set()
for key, value in all.items():
  if value == n:
    known.add(key)
    others.add(key)
  else:
    others.add(key)

print(len(known))
for word in known:
  print(word)

print(len(others))
for word in others:
  print(word)
