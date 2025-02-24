n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

all = [0]*(n+m)

n_last, m_last = -1, -1
n_pos, m_pos = 0, 0
N_best, M_best = 0, 0
r = 10**7

for i in range(n+m):
  if n_pos < n and m_pos < m: 
    if n_arr[n_pos] < m_arr[m_pos]:
      all[i] = n_arr[n_pos]
      n_pos += 1
      n_pos = min(n_pos, n)
      n_last = i
    else:
      all[i] = m_arr[m_pos]
      m_pos += 1 
      m_pos = min(m_pos, m)
      m_last = i

  elif m_pos == m:
    all[i] = n_arr[n_pos]
    n_last = i

  elif n_pos == n:
    all[i] = m_arr[m_pos]
    m_last = i

  if i > 0 and abs(n_last - m_last) == 1:
    if r > abs(all[n_last] - all[m_last]):
      N_best = all[n_last]
      M_best = all[m_last]
      r = abs(all[n_last] - all[m_last])
      if r == 0:
        break

print(N_best, M_best)
  