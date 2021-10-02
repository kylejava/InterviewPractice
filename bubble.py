def bubble(data):

    if(len(data) == 0 or len(data) == 1):
        return data

    flag = True
    while(flag == True):
        flag = False
        for i in range(len(data) - 1):
            if(data[i] > data[i + 1]):
                num = data[i]
                data[i] = data[i+1]
                data[i+1] = num
                flag = True

    return data


nums = [5,2,8,1,8,0,3,1,7,9]
data = bubble(nums)
print(data)
