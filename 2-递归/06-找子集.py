"""
给定一个集合，找出所有的子集
"""
def subset(nums):
    result = [[]]
    for num in nums:
        for element in result[:]:
            x = element[:]
            x.append(num)
            result.append(x)
    return result

nums = [1,2,3]
print(subset(nums))