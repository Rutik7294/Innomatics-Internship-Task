#min and max

import numpy


n,m= map(int, input().split())
a= [list(map(int,input().split())) for i in range(n)]
print(max(numpy.min(a,axis=1)))
