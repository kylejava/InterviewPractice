# Window Sliding Technique
# Given an array of size n, find the maximum sum of k consecutive elements in the array
# Assume there will always be an answer and that n is greater than 2
nums = [100,200,300,400]
k = 2

def calc(nums, k):
    left = 0
    right = k -1
    highest = 0
    window = 0
    for i in range(k):
        highest = highest+nums[i]

    window = highest

    while (right < len(nums)-1):

        window = window - nums[left]
        left += 1
        right +=  1
        window = window + nums[right]
        if(window > highest):
            highest = window

    print(highest)



calc(nums,k)
