#re.start(),re.end()

a = input()
b = input()
import re
pattern = re.compile(b)
m = pattern.search(a)
if not m: print("(-1, -1)")
while m:
    print("({0}, {1})".format(m.start(), m.end() - 1))
    m = pattern.search(a,m.start() + 1)
