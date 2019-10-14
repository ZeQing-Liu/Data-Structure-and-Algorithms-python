"""
给出一个长度为n的整数数组，数字的范围是1-n，
有些数字重复了而有些数字没有出现过，找出没有出现的数字
要求时间复杂度为o(n)
比如：
input：[4,3,2,7,8,2,3,1]
output：[5,6]
"""
import time
import matplotlib.pyplot as plt
import random
import math

# o(n^2)
def find_disa_num1(nums):
    result = []
    for i in range(1, len(nums)+1):
        if (i not in nums):
            result.append(i)
    return result

def find_disa_num1_test(nums):
    start = time.time()
    r = find_disa_num1(nums)
    t = time.time() - start
    return r, len(nums), t

def random_list(l):
    return [[i+1 for i in range(l * n)] for n in range(1, 20)]

random_lists = random_list(100)
rst = [find_disa_num1_test(l) for l in random_lists]
x = list(zip(*rst))[1]
y = list(zip(*rst))[2]
plt.plot(x,y)
plt.show()



def find_disa_num2(nums):
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = - abs(nums[index])
    return [i + 1 for i in range(len(nums)) if nums[i] > 0]
nums = [4,3,2,7,8,2,3,1]
print(find_disa_num2(nums))
