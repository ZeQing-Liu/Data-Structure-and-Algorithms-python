def grey_code1(n):
   if n==0:
       return
   grey_code1(n-1)
   print(n)
   grey_code1(n-1)

def grey_code2(n,forward):
    if n == 0:
        return
    grey_code2(n-1,True)
    print("enter ",n) if forward else print("exit  ",n)
    grey_code2(n-1,False)

grey_code1(4)
grey_code2(4,True)