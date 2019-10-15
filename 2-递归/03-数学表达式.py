"""
给定两个整数a<=b,写一个程序，通过a加1或乘以2，
以最少的次数得到b，如：
113 = ((((11 + 1) + 1) + 1) * 2 * 2 * 2 + 1)
"""
def intSeq(a,b):
    if (a == b):
        return str(a)

    if (b < a * 2):
        return "(" + intSeq(a,b-1) + " + 1)"

    if (b % 2 == 1):
        return "(" + intSeq(a,b-1) + " + 1)"

    return intSeq(a, b/2) + " * 2"

a = 11
b = 113
print(str(b) + " = " + intSeq(a,b))
