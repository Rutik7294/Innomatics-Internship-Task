#set.symmetric_difference()

n=int(input())
m=set(map(int,input().split()))
p=int(input())
q=set(map(int,input().split()))

ans=m.symmetric_difference(q)
print(len(ans))
