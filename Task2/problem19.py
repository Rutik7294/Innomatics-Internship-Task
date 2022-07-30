#Lists

if __name__ == '__main__':
    N = int(input())
    mt= []
    c = []

    for i in range(N):
        x = input().split()
        mt.append(x)

    for i in range(len(mt)):
        if mt[i][0] == 'insert':
            x = int(mt[i][1])
            y = int(mt[i][2])
            c.insert(x,y)
        elif mt[i][0] == 'print':
            print(c)
        elif mt[i][0] == 'remove':
            c.remove(int(mt[i][1]))
        elif mt[i][0] == 'append':
            c.append(int(mt[i][1]))
        elif mt[i][0] == 'sort':
            c.sort()
        elif mt[i][0] == 'pop':
            c.pop()
        elif mt[i][0] == 'reverse':
            c.reverse()
