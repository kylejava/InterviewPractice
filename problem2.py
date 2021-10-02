# Given an integer, convert it to binary

def solution(num):
    if(num == 0 or num == 1):
        return num

    
    ans = ""
    while num > 0:
        bit = num % 2
        if(bit == 1):
            ans += str(1)
        else:
            ans += str(0)
        
        num = num / 2

    
    return ans[::-1]

print(solution(10))


print(solution(16))

print(solution(25))
