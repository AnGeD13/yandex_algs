N, K, M = map(int, input().split())

counts = 0
if N >= K >= M > 0: 
  while N // K > 0:
    val_z = N // K
    counts += (K // M) * val_z
    N = N % K + val_z * (K % M)

print(counts)
