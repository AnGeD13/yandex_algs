def onlyOneUpperCase(word):
  arr = list(word)
  k = 0
  for i in range(len(arr)):
    if arr[i] == arr[i].upper():
      k += 1
      if k > 1:
        return False
  if k == 1:
    return True
  if k == 0:
    return False

n = int(input())
dict = {}
for i in range(n):
  word = input()
  wordKey = word.lower()
  if wordKey not in dict:
    dict[wordKey] = [word]
  else:
    dict[wordKey].append(word) 

sentence = input().split()
mistakes = 0
for word in sentence:
  wordLower = word.lower()
  if not onlyOneUpperCase(word):
    mistakes += 1
  elif wordLower in dict:
    if word not in dict[wordLower]:
      mistakes += 1
  elif word == wordLower:
    mistakes += 1

print(mistakes)
