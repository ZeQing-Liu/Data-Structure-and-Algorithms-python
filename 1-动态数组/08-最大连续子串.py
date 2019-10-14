"""
给一个只包含0和1的数组，
找出最长的全是1的子数组，返回长度
"""
def find_consecutive_ones(nums):
    local = maximum = 0
    for i in nums:
        local = local + 1 if i == 1 else 0
        maximum = max(maximum, local)
    return maximum

nums = [1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,1]
result = find_consecutive_ones(nums)
print(result)
