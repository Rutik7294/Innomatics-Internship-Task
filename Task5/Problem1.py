#detect floating point numbers

import re
for _ in range(int(input())):
    print(re.search(r'^([-\+])?\d*\.\d+$', input()) is not None)
