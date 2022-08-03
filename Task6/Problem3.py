#concatenate

import numpy

n,m,p= map(int,input().split())
x= numpy.array([input().split() for _ in range(n)],int)
y= numpy.array([input().split() for _ in range(m)],int)
print(numpy.concatenate((x,y), axis = 0))
