n = int(input())
sins = {}
for i in range(n):
  key, value = map(str, input().split())
  sins[key] = value

word = input()

if sins.get(word):
  print(sins[word])
else:
  for key in sins:
    if word == sins[key]:
      print(key)
      break
