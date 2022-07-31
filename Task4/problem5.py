# find a string

def count_substring(string, sub_string):
    l1=len(string)
    l2=len(sub_string)
    c=0
    for i in range(l1-l2+1):
        if (string[i:(i+l2)]==sub_string):
            c+=1
    
    return c
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
