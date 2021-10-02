def mergesort(data):
    if(len(data) == 0 or len(data) == 1):
        return data

    mid = len(data) // 2
    a = data[:mid]
    b = data[mid:]
    a = mergesort(a)
    b = mergesort(b)
    return merge(a, b)

def merge(a, b):
    c = []
    while(len(a) != 0 and len(b) != 0):

        if(a[0] > b[0] ):
            c.append(b[0])
            b.pop(0)
        else:
            c.append(a[0])
            a.pop(0)

    for i in range(len(a)):
        c.append(a[0])
        a.pop(0)

    for j in range(len(b)):
        c.append(b[0])
        b.pop(0)

    return (c)



x = [9,4,1,7,3,8,3,1,0]
print(mergesort(x))
