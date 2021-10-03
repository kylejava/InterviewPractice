def binary(target, nums):
    low = 0
    high = len(nums) -1
    mid = 0

    while(low <= high):
        mid = (low+high) //2

        if(nums[mid] > target):
            mid = low-1
        elif(nums[mid] < target):
            mid = high+1
        else:
            return mid


data = [1,2,3,4,5,6,7,8,9]
target = 4
print(binary(target, data))
