#set mutations

if __name__ == '__main__':
    (_, a) = (int(input()),set(map(int, input().split())))
    b = int(input())
    for _ in range(b):
        (command, newSet) = (input().split()[0],set(map(int, input().split())))
        getattr(a, command)(newSet)

    print (sum(a))
