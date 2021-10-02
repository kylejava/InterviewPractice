
def perm(data):
    if(len(data) == 0):
        return []
    elif(len(data) == 1):
        return [data]
    else:
        l = []
        for i in range(len(data)):
            x = data[i]
            xs = data[:i] + data[i + 1:]
            for p in perm(xs):
                l.append([x] + p)
        return l

data = list('123')
for p in perm(data):
    print(p)
