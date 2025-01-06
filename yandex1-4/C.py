s = open('input.txt', 'r').read().splitlines()

dict = {}
max_k = 0
for line in s:
  l = line.split()
  for word in l:
    if word in dict:
      dict[word] += 1
    else:
      dict[word] = 1
    if dict[word] > max_k:
      max_k = dict[word]

cur_word = ''
for key in dict:
  if dict[key] == max_k:
    if cur_word == '':
      cur_word = key
    elif key < cur_word:
      cur_word = key

print(cur_word)
