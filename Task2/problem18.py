#check strict superset

def isstrictsuperset(p,r):
    
    return r.issubset(p) and not(p.issubset(r))

p = set(int(x) for x in input().split(' '))
q = int(input())
res = True

for _ in range(q):
    r = set(int(x) for x in input().split(' '))
    res &= isstrictsuperset(p,r)
    
print(res)
