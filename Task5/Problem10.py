#hex color code
import re
a=int(input())

for i in range(0,a):
    p=input()

    x=p.split()

    if len(x)>1  and  '{' not in x:
        x=re.findall(r'#[a-fA-F0-9]{3,6}',p)
        [print(i) for  i in x]
