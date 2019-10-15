"""
输入n，输出斐波那契数列中对应位置的数字
"""
def fibonacci1(n):
    assert(n>0)
    a, b = 0, 1
    for i in range(1, n+1):
        a, b = b, a + b
    return a
def fibonacci2(n):
    assert(n>0)
    if (n <= 2):
        return 1
    return fibonacci2(n-1) + fibonacci2(n-2)

def fibonacci3(n):
    assert(n>0)
    if (n==1):
        return (n,0)
    (a,b) = fibonacci3(n-1)
    return (a + b, a)

def test_fibo(func):
    assert func(2) == 1
    assert func(6) == 8
    print("测试通过")

test_fibo(fibonacci1)
print(fibonacci1(40))