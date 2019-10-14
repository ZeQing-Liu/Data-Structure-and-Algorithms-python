def reverse1(s):
    return s[::-1]

def reverse2(s):
    l = list(s)
    for i in range(len(l) // 2):
        l[i],l[len(s)-1-i] = l[len(s)-1-i], l[i]
    return ''.join(l)


s = 'hello'
print(reverse1(s))
print()
print(reverse2(s))
