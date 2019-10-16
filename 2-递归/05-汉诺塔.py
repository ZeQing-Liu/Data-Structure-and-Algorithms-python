"""
一 3根圆柱A，B，C，其中A上面串了n个圆盘
二 这些圆盘从上到下是按从小到大顺序排列的，
   大的圆盘任何时刻不得位于小的圆盘上面
三 每次移动一个圆盘，最终实现将所有圆盘移动到Ｃ上
"""
def hanoi(n, start,by,end):
    if (n==1):
        print("Move from " + start + " to " + end)
    else:
        hanoi(n-1, start, end, by)
        hanoi(1, start, by, end)
        hanoi(n-1, by, start, end)
n = 3
hanoi(n, "START", "BY","END")