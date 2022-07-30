# check subset

n=int(input())
for i in range (n):
    a=input()
    A=set(input().split())
    b=int(input())
    B=set(input().split())
    print(A.issubset(B))
