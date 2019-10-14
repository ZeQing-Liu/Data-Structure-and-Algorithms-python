"""
把一个非负整数表示成一个列表，如123表示为[1,2,3]
给这个整数加1，返回一个新列表
"""
#coding:utf-8

def plus_one(digits):
    if len(digits) == 0:
        return False

    for i in range(len(digits)-1,-1,-1):
        digits[i] += 1
        if digits[i] == 10:
            digits[i] =0
            if i == 0:
                digits.insert(0,1)
        else:
            break
    return digits

digits1 = [8,8,9]
digits2 = [8,9,9]
digits3 = [9,9,9]
digits4 = [8,8,8]
print(plus_one(digits1))
print(plus_one(digits2))
print(plus_one(digits3))
print(plus_one(digits4))