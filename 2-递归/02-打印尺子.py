"""
输入数字1/2/3/4，打印如下图形
1
1 2 1
1 2 1 3 1 2 1
1 2 1 3 1 2 1 4 1 2 1 3 1 2 1
"""
# o(n)
def ruler1(n):
    assert(n>=0)
    if (n==1):
        return '1'
    t = ruler1(n-1)
    return t + " " + str(n) + " " + t

def ruler2(n):
    result = ""
    for i in range(1,n+1):
        result = result + str(i) + " " + result
    return result

print(ruler1(4))
print(ruler2(4))