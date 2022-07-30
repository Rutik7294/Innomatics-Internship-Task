#set.union()

n=int(input())
m=set(map(int,input().split()))
p=int(input())
q=set(map(int,input().split()))

ans=m.union(q)
c=0
for i in ans:
    c+=1
print(c)    
