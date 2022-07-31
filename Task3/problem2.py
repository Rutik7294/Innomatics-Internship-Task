#Find angle mbc

import math
ab=int(input())
bc=int(input())
m=math.atan(ab/bc)
n=round(math.degrees(m))
print(n,chr(176),sep='')
