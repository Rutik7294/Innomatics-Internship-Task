# The captains room

m =input()
a =input().split()
s=set()
t=set()
for i in a:
    if i not in s:
        s.add(i)
        t.add(i)
    else:
        t.discard(i)
print(t.pop())
