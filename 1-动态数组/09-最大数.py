"""
给定一个数组，数组里有且只有一个最大数，
判断这个最大数是否是其他数的两倍或更大。
如果存在这个数，则返回inde，否则返回-1
"""
def largest_twice(nums):
    maximum = second = idx = 0
    for i in range(len(nums)):
        if (maximum < nums[i]):
            second = maximum
            maximum = nums[i]
            idx = i
        elif second < nums[i]:
            second = nums[i]
    return idx if (maximum >= second * 2) else -1

nums = [1, 2, 3, 8, 3, 2, 1]
result = largest_twice(nums)
print(result)