n = int(input())
blocks = {}
for i in range(n):
  w, h = map(int, input().split())
  if w not in blocks:
    blocks[w] = h
  else:
    blocks[w] = max(blocks[w], h)
  
k = 0
for key in blocks:
  k += blocks[key]

print(k)
