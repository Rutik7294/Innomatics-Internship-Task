#set.intersection()

n=int(input())
m=set(map(int,input().split()))
p=int(input())
q=set(map(int,input().split()))

ans=m.intersection(q)

print(len(ans)) 
    
