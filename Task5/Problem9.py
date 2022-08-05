#validating and parsing email address

import re
a = int(input())
for _ in range(a):
    p, q = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', q)
    if m:
        print(p,q)
