def binary(target, nums):
    low = 0
    high = len(nums) -1
    mid = 0

    while(low <= high):
        mid = (low+high) //2
        print("low" + str(low))
        print("high" + str(high))
        if(nums[mid] > target):
            low = low -1
        elif(nums[mid] < target):
            high = high + 1
        else:
            return mid


data = [1,2,3,4,5,6,7,8,9]
target = 4
print(binary(target, data))
