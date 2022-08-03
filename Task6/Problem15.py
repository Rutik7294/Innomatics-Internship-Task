#min var std

import numpy as np
n, m = map(int, input().split())
k = np.array([input().split() for _ in range(n)],dtype = int)

print(np.mean(k,axis=1))
print(np.var(k,axis=0))
op=np.std(k)
print(np.round(np.std(k),11))
